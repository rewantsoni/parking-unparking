from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand
from sqlalchemy import Column, Integer, String, Boolean, DATE
import time
import grpc
import Protos.admin_parking_pb2
import Protos.admin_parking_pb2_grpc

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgres+psycopg2://postgres:@localhost:5432/parking'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
migrate = Migrate(app, db)
manager = Manager(app)
manager.add_command('db', MigrateCommand)


class Parking(db.Model):
    __tablename__ = 'parking'

    parking_id = Column(Integer(), primary_key=True, autoincrement=True)
    user_id = Column(String(10), nullable=False)
    car_id = Column(String(10), nullable=False)
    date_in = Column(DATE)
    date_out = Column(DATE)
    location = Column(String(10), nullable=False)
    isparked = Column(Boolean)

    def __init__(self, user_id, car_id, date_in, location, isparked):
        self.user_id = user_id
        self.car_id = car_id
        self.location = location
        self.date_in = date_in
        self.isparked = isparked


def check_car(car):
    return Parking.query.filter_by(car_id=car, isparked=True).first()


def parking(request, location):
    if check_car(request.carId.carId) is None:
        x = int(location / (4 * 10))
        y = int((location - (x * 4 * 10)) / 10)
        z = int((location - (x * 4 * 10) - (y * 10)))
        loc = 'L{}S{}F{}'.format(x, y, z)
        park = Parking(
            user_id=request.userId,
            car_id=request.carId.carId,
            location=loc,
            date_in=time.ctime(),
            isparked=True,
        )
        try:
            db.session.add(park)
            db.session.flush()
            db.session.commit()
            channel = grpc.insecure_channel('192.168.99.101:31743')
            print('connected')
            client = Protos.admin_parking_pb2_grpc.adminParkingApiStub(channel)
            print(client)
            client.insert(Protos.admin_parking_pb2.toInsert(userId=request.userId, carId=request.carId.carId,
                                                            location=loc, dateIn=time.ctime(), isparked=True))
            print('done')
            channel.close()
            db.session.close()
            return loc
        except Exception as e:
            raise e


def check_car_in_location(request):
    return Parking.query.filter_by(car_id=request.carId.carId, isparked=True,
                                   location=request.location.location).first()


def un_park_car(request):
    result = Parking.query.filter_by(car_id=request.carId.carId, isparked=True,
                                     location=request.location.location).first()
    if result is None:
        return result
    result.isparked = False
    result.date_out = time.ctime()
    db.session.flush()
    db.session.commit()
    channel = grpc.insecure_channel('192.168.99.101:31843')
    client = Protos.admin_parking_pb2_grpc.adminParkingApiStub(channel)
    client.update(Protos.admin_parking_pb2.toUpdate(carId=request.carId.carId, loc=request.location.location,
                                                    dateOut=time.ctime()))
    channel.close()
    return result


def check_user_car(request):
    return (Parking.query.filter_by(car_id=request.carId.carId, isparked=True,
                                    user_id=request.userId).first())


def return_error(context, error_code, error_details):
    context.set_code(error_code)
    context.set_details(error_details)
    raise grpc.RpcError


def un_parking(request, context):
    if check_car(request.carId.carId) is None:
        return_error(context, grpc.StatusCode.UNAVAILABLE, 'Car not in Parking')
    if check_user_car(request) is None:
        return_error(context, grpc.StatusCode.UNAVAILABLE, 'Different user parked the car')
    if check_car_in_location(request) is None:
        return_error(context, grpc.StatusCode.UNAVAILABLE, 'Car not in Location')
    un_park_car(request)
    return 'Car un-parked'


def serve():
    manager.run()

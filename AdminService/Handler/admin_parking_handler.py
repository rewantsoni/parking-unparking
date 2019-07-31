from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand
from sqlalchemy import Column, Integer, String, Boolean, DATE
import grpc

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgres+psycopg2://postgres:postgres@parkingdbmirror:5432/parking-mirror'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
migrate = Migrate(app, db)
manager = Manager(app)
manager.add_command('db', MigrateCommand)


def return_error(context, error_code, error_details):
    context.set_code(error_code)
    context.set_details(error_details)
    raise grpc.RpcError


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


def result(res, context):
    db.session.flush()
    db.session.commit()
    db.session.close()
    try:
        print(res[0])
        return res
    except IndexError:
        return_error(context, grpc.StatusCode.NOT_FOUND, 'Car not found')


def get_all(context):
    return result(Parking.query.all(), context)


def get_all_parked(context):
    return result(Parking.query.filter_by(isparked=True).all(), context)


def get_all_car_parked_by_date(context, date):
    return result(Parking.query.filter_by(date_in=date).all(), context)


def get_all_car_by_location(location, context):
    return result(Parking.query.filter_by(location=location).all(), context)


def get_car_parking_details(car, context):
    return result(Parking.query.filter_by(car_id=car).all(), context)


def get_car_by_location_currently_parked(location, context):
    return result(Parking.query.filter_by(location=location, isparked=True).all(), context)


def get_car_by_location_car_id(request, context):
    res = Parking.query.filter_by(location=request.location.location,
                                  car_id=request.carId.carId, isparked=True).first()
    if res is None:
        return_error(context, grpc.StatusCode.NOT_FOUND, 'Car not found')


def serve():
    manager.run()

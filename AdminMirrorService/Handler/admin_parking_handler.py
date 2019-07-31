from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand
from sqlalchemy import Column, Integer, String, Boolean, DATE

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgres+psycopg2://postgres:postgres@parkingdbmirror:5432/parking-mirror'
# app.config['SQLALCHEMY_DATABASE_URI'] = 'postgres+psycopg2://postgres:@localhost:5432/parking_mirror'
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


def insert(request):
    park = Parking(
        user_id=request.userId,
        car_id=request.carId,
        location=request.location,
        date_in=request.dateIn,
        isparked=True,
    )
    db.session.add(park)
    db.session.flush()
    db.session.commit()
    db.session.close()


def update(request):
    result = Parking.query.filter_by(car_id=request.carId, isparked=True,
                                     location=request.loc).first()
    result.isparked = False
    result.date_out = request.dateOut
    db.session.flush()
    db.session.commit()


def serve():
    manager.run()

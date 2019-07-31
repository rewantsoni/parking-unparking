from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand
from sqlalchemy import Column, Integer, String, Boolean, DATE

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgres+psycopg2://postgres:@localhost:5432/notifydb'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
migrate = Migrate(app, db)
manager = Manager(app)
manager.add_command('db', MigrateCommand)


class Notify(db.Model):
    __tablename__ = 'notify'

    user_id = Column(String(10), nullable=False, primary_key=True)
    parking_count = Column(Integer, nullable=False)

    def __init__(self, user_id, parking_count):
        self.user_id = user_id
        self.parking_count = parking_count


def insert(user_id):
    notify = Notify(
        user_id=user_id,
        parking_count=1
    )
    db.session.add(notify)
    db.session.flush()
    db.session.commit()
    db.session.close()


def update(user_id):
    result = Notify.query.filter_by(user_id=user_id).first()
    result.parking_count = result.parking_count + 1
    db.session.flush()
    db.session.commit()


def check_user_exists(user_id):
    result = Notify.query.filter_by(user_id=user_id).first()
    return result


def get_count(user_id):
    return Notify.query.filter_by(user_id=user_id).first().parking_count


def reset(user_id):
    result = Notify.query.filter_by(user_id=user_id).first()
    result.parking_count = 0
    db.session.flush()
    db.session.commit()


def serve():
    manager.run()


if __name__ == "__main__":
    manager.run()

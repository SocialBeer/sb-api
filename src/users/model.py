import sqlalchemy as db

from ..database import Base, engine


class UserModel(Base):
    __tablename__ = 'Users'

    id = db.Column(db.Integer, primary_key = True, index = True)
    email = db.Column(db.String(100), unique = True)
    first_name = db.Column(db.String(50))
    last_name = db.Column(db.String(50))
    country = db.Column(db.String(50))
    password_hash = db.Column(db.String(128))

UserModel.__table__.create(engine, checkfirst = True)

import sqlalchemy as db
from ..database import Base


class UserModel(Base):
    __tablename__ = 'Users'

    id = db.Column(db.Integer, primary_key = True)
    username = db.Column(db.String(50), unique = True)
    password_hash = db.Column(db.String(128))
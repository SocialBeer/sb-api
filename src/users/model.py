import sqlalchemy as db
from ..models import Base


class UserModel(Base):
    __tablename__ = 'Users'

    id = db.Column(db.Integer, primary_key = True)
    username = db.Column(db.String(50))
    password_hash = db.Column(db.String(128))



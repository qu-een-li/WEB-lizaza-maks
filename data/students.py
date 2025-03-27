import datetime
import sqlalchemy
from sqlalchemy import orm

from .db_session import SqlAlchemyBase


class Student(SqlAlchemyBase):
    __tablename__ = 'students'
    id = sqlalchemy.Column(sqlalchemy.Integer,
                           primary_key=True, autoincrement=True)
    name = sqlalchemy.Column(sqlalchemy.String, nullable=True)
    age = sqlalchemy.Column(sqlalchemy.Integer, nullable=True)
    birthday = sqlalchemy.Column(sqlalchemy.String, nullable=True)
    PFDO = sqlalchemy.Column(sqlalchemy.Integer, nullable=True)
    address = sqlalchemy.Column(sqlalchemy.String, nullable=True)
    member_phone = sqlalchemy.Column(sqlalchemy.Integer, nullable=True)
    school_class = sqlalchemy.Column(sqlalchemy.Integer, nullable=True)
    name_OO = sqlalchemy.Column(sqlalchemy.String, nullable=True)
    city_OO = sqlalchemy.Column(sqlalchemy.String, nullable=True)

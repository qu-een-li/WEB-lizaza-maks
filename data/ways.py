import datetime
import sqlalchemy
from sqlalchemy import orm

from .db_session import SqlAlchemyBase


class Way(SqlAlchemyBase):
    __tablename__ = 'ways'
    id = sqlalchemy.Column(sqlalchemy.Integer,
                           primary_key=True, autoincrement=True)
    PFDO = sqlalchemy.Column(sqlalchemy.Integer, nullable=True)
    Programming_in_Python = sqlalchemy.Column(sqlalchemy.String, nullable=True)
    Fundamentals_of_algorithmics_and_logic = sqlalchemy.Column(sqlalchemy.String, nullable=True)
    Mobile_development = sqlalchemy.Column(sqlalchemy.String, nullable=True)
    Website_development = sqlalchemy.Column(sqlalchemy.String, nullable=True)
    Machine_learning = sqlalchemy.Column(sqlalchemy.String, nullable=True)
    VR_AR_Application_Development = sqlalchemy.Column(sqlalchemy.String, nullable=True)
    System_administration = sqlalchemy.Column(sqlalchemy.String, nullable=True)
    The_basics_of_computer_fiction = sqlalchemy.Column(sqlalchemy.String, nullable=True)
    Programming_robots = sqlalchemy.Column(sqlalchemy.String, nullable=True)

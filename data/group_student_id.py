import datetime
import sqlalchemy
from sqlalchemy import orm

from .db_session import SqlAlchemyBase


class Group_Student_id(SqlAlchemyBase):
    __tablename__ = 'group_student_id'
    id = sqlalchemy.Column(sqlalchemy.Integer,
                           primary_key=True, autoincrement=True)
    id_group = sqlalchemy.Column(sqlalchemy.Integer, nullable=True)
    id_student = sqlalchemy.Column(sqlalchemy.Integer, nullable=True)

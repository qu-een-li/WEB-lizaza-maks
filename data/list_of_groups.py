import datetime
import sqlalchemy
from sqlalchemy import orm

from .db_session import SqlAlchemyBase


class Group(SqlAlchemyBase):
    __tablename__ = 'groups'
    id = sqlalchemy.Column(sqlalchemy.Integer, sqlalchemy.ForeignKey("group_student_id.id_group"),
                           primary_key=True, autoincrement=True)
    name_of_group = sqlalchemy.Column(sqlalchemy.String, nullable=True)
    id_teacher = sqlalchemy.Column(sqlalchemy.Integer, nullable=True)
    id_way = sqlalchemy.Column(sqlalchemy.Integer, nullable=True)
    year = sqlalchemy.Column(sqlalchemy.String, nullable=True)
    half_a_year = sqlalchemy.Column(sqlalchemy.Integer, nullable=True)


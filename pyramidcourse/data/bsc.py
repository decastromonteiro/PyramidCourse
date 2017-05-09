import sqlalchemy
from pyramidcourse.data.modelbase import SqlAlchemyBase


class BSC(SqlAlchemyBase):
    __tablename__ = 'BSC'

    id = sqlalchemy.Column(sqlalchemy.Integer, primary_key=True, autoincrement=True)
    name = sqlalchemy.Column(sqlalchemy.String)
    date_added = sqlalchemy.Column(sqlalchemy.DateTime)
    active = sqlalchemy.Column(sqlalchemy.Boolean)

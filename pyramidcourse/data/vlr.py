import sqlalchemy
import sqlalchemy.orm
from pyramidcourse.data.modelbase import SqlAlchemyBase


class VLR(SqlAlchemyBase):
    __tablename__ = 'VLR'

    id = sqlalchemy.Column(sqlalchemy.Integer, primary_key=True, autoincrement=True)
    date_added = sqlalchemy.Column(sqlalchemy.DateTime)
    vlr_name = sqlalchemy.Column(sqlalchemy.String, unique=True)
    vlr_number = sqlalchemy.Column(sqlalchemy.String, unique=True)

    # LocationAreaId Relationship
    lai = sqlalchemy.orm.relationship("LocationAreaId", back_populates="lai")

    active = sqlalchemy.Column(sqlalchemy.Boolean)

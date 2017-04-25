import sqlalchemy
from pyramidcourse.data.modelbase import SqlAlchemyBase


class VLR(SqlAlchemyBase):
    __tablename__ = 'VLR'

    id = sqlalchemy.Column(sqlalchemy.Integer, primary_key=True, autoincrement=True)
    date_added = sqlalchemy.Column(sqlalchemy.DateTime)
    vlr_name = sqlalchemy.Column(sqlalchemy.String, unique=True)
    vlr_number = sqlalchemy.Column(sqlalchemy.String, unique=True)
    lai = sqlalchemy.Column(sqlalchemy.String)  # todo backpopulate with location_area_identifier
    lac = sqlalchemy.Column(sqlalchemy.String)  # todo backpopulate with location_area_identifier
    active = sqlalchemy.Column(sqlalchemy.Boolean)

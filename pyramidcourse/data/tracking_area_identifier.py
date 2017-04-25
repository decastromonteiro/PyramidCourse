import sqlalchemy
from pyramidcourse.data.modelbase import SqlAlchemyBase

'''
TrackingAreaId table relationships

. Multiple TAI to one LAI
. One TAI to multiple SGSN (MME)

'''

class TrackingAreaId(SqlAlchemyBase):
    __tablename__ = 'TrackingAreaId'

    id = sqlalchemy.Column(sqlalchemy.Integer, primary_key=True, autoincrement=True)
    date_added = sqlalchemy.Column(sqlalchemy.DateTime)
    mcc = sqlalchemy.Column(sqlalchemy.String)
    mnc = sqlalchemy.Column(sqlalchemy.String)
    tac = sqlalchemy.Column(sqlalchemy.String)
    tai = sqlalchemy.Column(sqlalchemy.String, default=mcc + mnc + tac, unique=True)
    lai = sqlalchemy.Column(sqlalchemy.String)  # todo backpopulate with vlr
    vlr_name = sqlalchemy.Column(sqlalchemy.String)  # todo backpopulate with vlr
    vlr_number = sqlalchemy.Column(sqlalchemy.String)  # todo backpopulate with vlr
    sgsn_name = sqlalchemy.Column(sqlalchemy.String)  # todo backpopulate with sgsn
    active = sqlalchemy.Column(sqlalchemy.Boolean)


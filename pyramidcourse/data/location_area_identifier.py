import sqlalchemy
from pyramidcourse.data.modelbase import SqlAlchemyBase

'''
LocationAreaId table relationships

. One LAI to multiple TAI
. One LAI to one VLR (Huawei MME Limitation)
. Multiple LAI to one RNC
. Multiple LAI to one BSC


'''


class LocationAreaId(SqlAlchemyBase):
    __tablename__ = 'LocationAreaId'

    id = sqlalchemy.Column(sqlalchemy.Integer, primary_key=True, autoincrement=True)
    mcc = sqlalchemy.Column(sqlalchemy.String)
    mnc = sqlalchemy.Column(sqlalchemy.String)
    lac = sqlalchemy.Column(sqlalchemy.String)
    rac = sqlalchemy.Column(sqlalchemy.String)
    lai = sqlalchemy.Column(sqlalchemy.String, default=mcc + mnc + lac, unique=True)
    vlr_number = sqlalchemy.Column(sqlalchemy.String, nullable=True)
    vlr_name = sqlalchemy.Column(sqlalchemy.String, nullable=True)
    tai = sqlalchemy.Column(sqlalchemy.String, nullable=True)
    bsc_name = sqlalchemy.Column(sqlalchemy.String, nullable=True)
    rnc_name = sqlalchemy.Column(sqlalchemy.String, nullable=True)
    active = sqlalchemy.Column(sqlalchemy.Boolean)

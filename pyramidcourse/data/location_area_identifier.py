import sqlalchemy
import sqlalchemy.orm
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
    lai = sqlalchemy.Column(sqlalchemy.String, default=mcc + mnc + lac, unique=True)

    # TrackingAreaId Relationship
    tai = sqlalchemy.orm.relationship("TrackingAreaId", back_populates="tai")

    # RoutingAreaCode Relationship
    rac = sqlalchemy.orm.relationship("RoutingAreaCode", back_populates="rac")

    # VLR Relationship
    vlr_id = sqlalchemy.Column(sqlalchemy.Integer, sqlalchemy.ForeignKey("VLR.id"))
    vlr_name = sqlalchemy.orm.relationship('VLR', back_populates='vlr_name')
    vlr_number = sqlalchemy.orm.relationship('VLR', back_populates='vlr_number')

    # BSC Relationship
    bsc_id = sqlalchemy.Column(sqlalchemy.Integer, sqlalchemy.ForeignKey("BSC.id"))
    bsc_name = sqlalchemy.orm.relationship('BSC', back_populates='bsc_name')

    # RNC Relationship
    rnc_id = sqlalchemy.Column(sqlalchemy.Integer, sqlalchemy.ForeignKey("RNC.id"))
    rnc_name = sqlalchemy.orm.relationship('RNC', back_populates='rnc_name')

    active = sqlalchemy.Column(sqlalchemy.Boolean)

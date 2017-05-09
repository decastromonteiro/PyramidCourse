import sqlalchemy
import sqlalchemy.orm
from pyramidcourse.data.modelbase import SqlAlchemyBase

'''
LocationAreaId table relationships

. One LAI to Many TAI
. One LAI to One VLR (Huawei MME Limitation)
. Many LAI to Many RNC
. Many LAI to Many BSC

'''


class LocationAreaId(SqlAlchemyBase):
    __tablename__ = 'LocationAreaId'
    active = sqlalchemy.Column(sqlalchemy.Boolean)

    id = sqlalchemy.Column(sqlalchemy.Integer, primary_key=True, autoincrement=True)
    mcc = sqlalchemy.Column(sqlalchemy.String)
    mnc = sqlalchemy.Column(sqlalchemy.String)
    lac = sqlalchemy.Column(sqlalchemy.String, index=True)
    lai = sqlalchemy.Column(sqlalchemy.String, default=mcc + mnc + lac, unique=True, index=True)

    # TrackingAreaId Relationship
    # tai = sqlalchemy.orm.relationship("TrackingAreaId", back_populates="tai")

    # RoutingAreaCode Relationship
    rac = sqlalchemy.orm.relationship("RoutingAreaCode", back_populates="rac", cascade='all')

    # VLR Relationship
    # vlr_id = sqlalchemy.Column(sqlalchemy.Integer, sqlalchemy.ForeignKey("VLR.id"))
    # vlr_name = sqlalchemy.orm.relationship('VLR', back_populates='vlr_name')
    # vlr_number = sqlalchemy.orm.relationship('VLR', back_populates='vlr_number')

    # BSC Relationship
    # bsc_id = sqlalchemy.Column(sqlalchemy.Integer, sqlalchemy.ForeignKey("BSC.id"))
    # bsc_name = sqlalchemy.orm.relationship('BSC', back_populates='bsc_name')

    # RNC Relationship
    # rnc_id = sqlalchemy.Column(sqlalchemy.Integer, sqlalchemy.ForeignKey("RNC.id"))
    # rnc_name = sqlalchemy.orm.relationship('RNC', back_populates='rnc_name')



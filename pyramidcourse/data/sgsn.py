import sqlalchemy
import sqlalchemy.orm
from pyramidcourse.data.modelbase import SqlAlchemyBase

'''
SGSN table relationships

. Many SGSN to Many RNC
. Many SGSN to Many BSC
. Many SGSN to Many TrackingAreaId
. Many SGSN to Many VLR
'''


class SGSN(SqlAlchemyBase):
    __tablename__ = 'SGSN'

    # TrackingAreaId Relationship
    tai = sqlalchemy.orm.relationship('TrackingAreaId', back_populates='tai')

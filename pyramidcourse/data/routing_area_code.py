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


class RoutingAreaCode(SqlAlchemyBase):
    __tablename__ = 'RoutingAreaCode'

    id = sqlalchemy.Column(sqlalchemy.Integer, primary_key=True, autoincrement=True)
    rac = sqlalchemy.Column(sqlalchemy.String)

    # LocationAreaId Relationship
    lai_id = sqlalchemy.Column(sqlalchemy.Integer, sqlalchemy.ForeignKey("LocationAreaId.id"))
    lai = sqlalchemy.orm.relationship('LocationAreaId', back_populates='lai')

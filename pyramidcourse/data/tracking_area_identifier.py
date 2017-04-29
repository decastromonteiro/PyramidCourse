import sqlalchemy
import sqlalchemy.orm
from pyramidcourse.data.modelbase import SqlAlchemyBase

'''
TrackingAreaId table relationships

. Many TAI to One LAI
. Many TAI to Many SGSN

'''


class TrackingAreaId(SqlAlchemyBase):
    __tablename__ = 'TrackingAreaId'

    id = sqlalchemy.Column(sqlalchemy.Integer, primary_key=True, autoincrement=True)
    date_added = sqlalchemy.Column(sqlalchemy.DateTime)

    mcc = sqlalchemy.Column(sqlalchemy.String)
    mnc = sqlalchemy.Column(sqlalchemy.String)
    tac = sqlalchemy.Column(sqlalchemy.String)
    tai = sqlalchemy.Column(sqlalchemy.String, default=mcc + mnc + tac, unique=True)

    # LocationAreaId Relationship
    lai_id = sqlalchemy.Column(sqlalchemy.Integer, sqlalchemy.ForeignKey("LocationAreaId.id"))
    lai = sqlalchemy.orm.relationship("LocationAreaId", back_populates="lai")

    # SGSN Relationship
    sgsn_name = sqlalchemy.orm.relationship('SGSN', back_populates='sgsn_name')

    active = sqlalchemy.Column(sqlalchemy.Boolean)

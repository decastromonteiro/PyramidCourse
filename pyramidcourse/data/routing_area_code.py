import sqlalchemy
import sqlalchemy.orm
from pyramidcourse.data.modelbase import SqlAlchemyBase

'''
LocationAreaId table relationships

. Many RoutingAreaCode to One LocationAreaId

'''


class RoutingAreaCode(SqlAlchemyBase):
    __tablename__ = 'RoutingAreaCode'
    active = sqlalchemy.Column(sqlalchemy.Boolean)

    id = sqlalchemy.Column(sqlalchemy.Integer, primary_key=True, autoincrement=True)
    rac = sqlalchemy.Column(sqlalchemy.String, index=True)

    # LocationAreaId Relationship
    # lai_id = sqlalchemy.Column(sqlalchemy.Integer, sqlalchemy.ForeignKey("LocationAreaId.id"))
    # lac = sqlalchemy.orm.relationship('LocationAreaId', back_populates='lac')


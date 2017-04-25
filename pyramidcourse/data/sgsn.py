import sqlalchemy
from pyramidcourse.data.modelbase import SqlAlchemyBase

'''
SGSN table relationships

. One SGSN to multiple RNC
. 
'''


class SGSN(SqlAlchemyBase):
    __tablename__ = 'SGSN'

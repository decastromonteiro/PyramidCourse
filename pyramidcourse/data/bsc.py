import sqlalchemy
from pyramidcourse.data.modelbase import SqlAlchemyBase

import pyramidcourse.data.tracking_area_identifier
import pyramidcourse.data.bsc
import pyramidcourse.data.rnc
import pyramidcourse.data.vlr


class BSC(SqlAlchemyBase):
    __tablename__ = 'BSC'

    id = sqlalchemy.Column(sqlalchemy.Integer, primary_key=True, autoincrement=True)
    name = sqlalchemy.Column(sqlalchemy.String)
    date_added = sqlalchemy.Column(sqlalchemy.DateTime)
    active = sqlalchemy.Column(sqlalchemy.Boolean)

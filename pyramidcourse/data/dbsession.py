import sqlalchemy
from pyramidcourse.data.modelbase import SqlAlchemyBase
import pyramidcourse.data.vlr
import pyramidcourse.data.tracking_area_identifier
import pyramidcourse.data.rnc
import pyramidcourse.data.bsc

class DbSessionFactory:

    @staticmethod
    def global_init(db_file):
        if not db_file:
            raise Exception('You must specify a data file.')
        conn_str = 'sqlite:///' + db_file
        engine = sqlalchemy.create_engine(conn_str)
        SqlAlchemyBase.metadata.create_all(engine)


# coding=utf-8
import sqlalchemy
import sqlalchemy.orm
from pyramidcourse.data.modelbase import SqlAlchemyBase, AccountBase
# noinspection PyUnresolvedReferences
# import pyramidcourse.data.vlr
# noinspection PyUnresolvedReferences
# import pyramidcourse.data.tracking_area_identifier
# noinspection PyUnresolvedReferences
# import pyramidcourse.data.rnc
# noinspection PyUnresolvedReferences
# import pyramidcourse.data.bsc
# noinspection PyUnresolvedReferences
# import pyramidcourse.data.sgsn
# noinspection PyUnresolvedReferences
import pyramidcourse.data.account
# noinspection PyUnresolvedReferences
# import pyramidcourse.data.location_area_identifier
# noinspection PyUnresolvedReferences
import pyramidcourse.data.routing_area_code


class DbSessionFactory:
    factory = None
    usr_factory = None

    @staticmethod
    def global_init(db_file, user_db_file):
        if DbSessionFactory.factory:
            return

        if not db_file or not db_file.strip():
            raise Exception('You must specify a data file.')

        conn_str = 'sqlite:///' + db_file
        usr_conn_str = 'sqlite:///' + user_db_file

        engine = sqlalchemy.create_engine(conn_str, echo=False)
        usr_engine = sqlalchemy.create_engine(usr_conn_str, echo=False)

        SqlAlchemyBase.metadata.create_all(engine)
        AccountBase.metadata.create_all(usr_engine)

        DbSessionFactory.usr_factory = sqlalchemy.orm.sessionmaker(bind=usr_engine)
        DbSessionFactory.factory = sqlalchemy.orm.sessionmaker(bind=engine)

    @staticmethod
    def create_session():
        return DbSessionFactory.factory()

    @staticmethod
    def create_session_usr():
        return DbSessionFactory.usr_factory()

# coding=utf-8
from pyramidcourse.data.dbsession import DbSessionFactory
from pyramidcourse.data.routing_area_code import RoutingAreaCode


class RANService:
    @staticmethod
    def get_routing_area_code():
        session = DbSessionFactory.create_session()

        results = session.query(RoutingAreaCode) \
            .filter(RoutingAreaCode.rac) \
            .all()

        return results


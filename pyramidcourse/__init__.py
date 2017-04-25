import os

from pyramid.config import Configurator

import pyramidcourse
import pyramidcourse.controllers.home_controller as home
import pyramidcourse.controllers.ran_controller as ran
import pyramidcourse.controllers.account_controller as account
from pyramidcourse.data.dbsession import DbSessionFactory


def main(global_config, **settings):
    """ This function returns a Pyramid WSGI application.
    """
    config = Configurator(settings=settings)

    init_includes(config)
    init_routing(config)
    init_db(config)
    return config.make_wsgi_app()


def init_db(config):
    top_folder = os.path.dirname(pyramidcourse.__file__)
    rel_folder = os.path.join('db', 'network_elements.sqlite')

    db_file = os.path.join(top_folder, rel_folder)
    DbSessionFactory.global_init(db_file)


def init_includes(config):
    config.include('pyramid_jinja2')
    config.include('pyramid_handlers')


def init_routing(config):
    config.add_static_view('static', 'static', cache_max_age=3600)

    config.add_handler('root', '/', handler=home.HomeController, action='index')

    add_controller_routes(config, home.HomeController, 'home')
    add_controller_routes(config, ran.RanController, 'ran')
    add_controller_routes(config, account.AccountController, 'account')
    config.scan()


def add_controller_routes(config, ctrl, prefix):
    config.add_handler(prefix + 'ctrl_index', '/' + prefix, handler=ctrl, action='index')
    config.add_handler(prefix + 'ctrl_index/', '/' + prefix + '/', handler=ctrl, action='index')
    config.add_handler(prefix + 'ctrl', '/' + prefix + '/{action}', handler=ctrl)
    config.add_handler(prefix + 'ctrl/', '/' + prefix + '/{action}/', handler=ctrl)
    config.add_handler(prefix + 'ctrl_id', '/' + prefix + '/{action}/{id}', handler=ctrl)

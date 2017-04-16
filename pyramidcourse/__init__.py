from pyramid.config import Configurator
import pyramidcourse.controllers.home_controller as home

def main(global_config, **settings):
    """ This function returns a Pyramid WSGI application.
    """
    config = Configurator(settings=settings)

    init_includes(config)
    init_routing(config)
    return config.make_wsgi_app()


def init_includes(config):
    config.include('pyramid_jinja2')
    config.include('pyramid_handlers')


def init_routing(config):
    config.add_static_view('static', 'static', cache_max_age=3600)

    config.add_handler('root', '/', handler=home.HomeController, action='index')
    config.add_handler('home_root', '/home', handler=home.HomeController, action='index')
    config.add_handler('home_root/', '/home/', handler=home.HomeController, action='index')
    config.add_handler('home_ctrl', '/home/{action}', handler=home.HomeController)
    config.add_handler('home_ctrl/', '/home/{action}/', handler=home.HomeController)

    config.scan()

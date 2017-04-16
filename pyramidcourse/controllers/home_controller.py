import pyramid_handlers
from pyramidcourse.controllers.base_controller import BaseController
from pyramidcourse.infrastructure.supressor import suppress


class HomeController(BaseController):
    @pyramid_handlers.action(renderer='/templates/home/home.jinja2')
    def index(self):
        return {'project': 'INDEX',
                'author': 'Leonardo de Castro Monteiro'}

    @pyramid_handlers.action(renderer='/templates/home/about.jinja2')
    def about(self):
        return {'project': 'ABOUT',
                'author': 'Leonardo de Castro Monteiro'}

    @pyramid_handlers.action(renderer='/templates/home/contact.jinja2')
    def contact(self):
        return {'project': 'CONTACT',
                'author': 'Leonardo de Castro Monteiro'}

    @suppress
    def teste(self):
        return {'project': 'lol'}

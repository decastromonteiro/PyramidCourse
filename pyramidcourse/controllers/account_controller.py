import pyramid_handlers
from pyramidcourse.controllers.base_controller import BaseController
from pyramidcourse.infrastructure.supressor import suppress
from pyramidcourse.viewmodels.accountviewmodel import AccountViewModel
from pyramidcourse.viewmodels.registerviewmodel import RegisterViewModel


class AccountController(BaseController):
    @pyramid_handlers.action(renderer='/templates/account/index.jinja2')
    def index(self):
        viewmodel = AccountViewModel()
        return viewmodel.to_dict()

    # Register GET Method
    @pyramid_handlers.action(renderer='/templates/account/register.jinja2',
                             request_method='GET',
                             name='register')
    def register_get(self):
        viewmodel = RegisterViewModel()
        return viewmodel.to_dict()

    # Register POST Method
    @pyramid_handlers.action(renderer='/templates/account/register.jinja2',
                             request_method='POST',
                             name='register')
    def register_post(self):
        viewmodel = RegisterViewModel()
        viewmodel.from_dict(self.request.POST)

        viewmodel.validate()
        if viewmodel.error:
            return viewmodel.to_dict()

        self.redirect('/account')

    # Sign In GET Method
    @pyramid_handlers.action(renderer='/templates/account/signin.jinja2',
                             request_method='GET',
                             name='signin')
    def signin_get(self):
        return {}

    # Sign In POST Method
    @pyramid_handlers.action(renderer='/templates/account/signin.jinja2',
                             request_method='POST',
                             name='signin')
    def signin_post(self):
        return {}

    @suppress
    def teste(self):
        return {'project': 'lol'}

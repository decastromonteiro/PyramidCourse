# coding=utf-8
import pyramid_handlers
from pyramidcourse.controllers.base_controller import BaseController
from pyramidcourse.services.account_service import AccountService
from pyramidcourse.viewmodels.registerviewmodel import RegisterViewModel
from pyramidcourse.viewmodels.signin_viewmodel import SigninViewModel
from pyramidcourse.viewmodels.accountviewmodel import AccountViewModel
import pyramidcourse.infrastructure.cookie_auth as cookie_auth


class AccountController(BaseController):
    @pyramid_handlers.action(renderer='/templates/account/index.jinja2',
                             request_method='GET',
                             name='index')
    def index_get(self):
        if not self.logged_in_user_id:
            print("Cannot view account page, must login")
            self.redirect('/account/signin')

        account = self.logged_in_user
        if account:
            return {'first_name': account.first_name,
                    'last_name': account.last_name
                    }

    @pyramid_handlers.action(renderer='/templates/account/index.jinja2',
                             request_method='POST',
                             name='index')
    def index_post(self):
        vm = AccountViewModel()
        vm.from_dict(self.request.POST)

        usr_id = self.logged_in_user_id

        AccountService.update_account_name(usr_id, vm.first_name, vm.last_name)

        return self.redirect('/account')

    @pyramid_handlers.action(renderer='/templates/account/signin.jinja2',
                             request_method='GET',
                             name='signin')
    def signin_get(self):
        if self.logged_in_user_id:
            self.redirect('/account')
        return SigninViewModel().to_dict()

    @pyramid_handlers.action(renderer='/templates/account/signin.jinja2',
                             request_method='POST',
                             name='signin')
    def signin_post(self):
        vm = SigninViewModel()
        vm.from_dict(self.request.POST)

        account = AccountService.get_authenticated_account(vm.email, vm.password)
        if not account:
            vm.error = "Email address or password are incorrect."
            return vm.to_dict()

        cookie_auth.set_auth(self.request, account.id)

        return self.redirect('/account')

    @pyramid_handlers.action()
    def logout(self):
        cookie_auth.logout(self.request)
        self.redirect('/')

    @pyramid_handlers.action(renderer='/templates/account/register.jinja2',
                             request_method='GET',
                             name='register')
    def register_get(self):
        vm = RegisterViewModel()
        return vm.to_dict()

    @pyramid_handlers.action(renderer='/templates/account/register.jinja2',
                             request_method='POST',
                             name='register')
    def register_post(self):
        vm = RegisterViewModel()
        vm.from_dict(self.request.POST)

        vm.validate()
        if vm.error:
            return vm.to_dict()

        account = AccountService.find_account_by_email(vm.email)
        if account:
            vm.error = "An account with this email already exists. " \
                       "Please log in instead."
            return vm.to_dict()

        account = AccountService.create_account(vm.email, vm.password)
        print("Registered new user: " + account.email)

        # send welcome email

        # redirect
        print("Redirecting to account index page...")
        self.redirect('/account')
        return account

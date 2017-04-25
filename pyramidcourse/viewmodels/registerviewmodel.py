from pyramidcourse.viewmodels.viewmodelbase import ViewModelBase
from re import match


class RegisterViewModel(ViewModelBase):
    def __init__(self):
        self.username = ""
        self.email = ""
        self.password = ""
        self.confirm_password = ""
        self.error = None

    def from_dict(self, data_dict):
        self.username = data_dict.get('username')
        self.email = data_dict.get('email')
        self.password = data_dict.get('password')
        self.confirm_password = data_dict.get('confirm_password')

    # noinspection PyMethodMayBeStatic
    def validate(self):
        self.error = None
        if not self.username:
            self.error = "The username field cannot be empty"
            return
        if match(r'anonymous', self.username, re.IGNORECASE):
            self.error = "Username cannot be Anonymous"
            return
        if not self.email:
            self.error = "The email field cannot be empty"
            return
        if self.password != self.confirm_password:
            self.error = "The password and confirmation don't match"
            return

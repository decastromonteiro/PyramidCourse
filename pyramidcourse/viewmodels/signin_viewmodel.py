from pyramidcourse.viewmodels.viewmodelbase import ViewModelBase


class SigninViewModel(ViewModelBase):
    def __init__(self):
        self.email = ""
        self.password = ""
        self.error = ""

    def from_dict(self, data_dict):
        self.email = data_dict.get('email')
        self.password = data_dict.get('password')

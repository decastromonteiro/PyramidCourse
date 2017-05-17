from pyramidcourse.viewmodels.viewmodelbase import ViewModelBase


class SigninViewModel(ViewModelBase):
    def __init__(self):
        self.email = ""
        self.password = ""
        self.error = ""
        self.usr_id = ""
        self.first_name = ""
        self.last_name = ""

    def from_dict(self, data_dict):
        self.email = data_dict.get('email')
        self.password = data_dict.get('password')

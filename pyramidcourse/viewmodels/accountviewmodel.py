from pyramidcourse.viewmodels.viewmodelbase import ViewModelBase


class AccountViewModel(ViewModelBase):
    def __init__(self):
        self.username = 'Anonymous'
        self.email = ""

    def from_dict(self, data_dict):
        self.username = data_dict.get('username')
        self.email = data_dict.get('email')

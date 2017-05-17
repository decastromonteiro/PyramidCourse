# coding=utf-8
from pyramidcourse.viewmodels.viewmodelbase import ViewModelBase


class AccountViewModel(ViewModelBase):
    def __init__(self):
        self.first_name = ""
        self.last_name = ""

    def from_dict(self, data_dict):
        self.first_name = data_dict.get('first_name')
        self.last_name = data_dict.get('last_name')

import sqlalchemy
from sqlalchemy import Column, String, DateTime, Boolean
from pyramidcourse.data.modelbase import AccountBase
import datetime
import uuid

'''

'''


class Account(AccountBase):
    __tablename__ = 'Account'

    id = Column(String, primary_key=True,
                default=lambda: str(uuid.uuid4()).replace('-', ''))

    email = Column(String, index=True, unique=True, nullable=False)
    password_hash = Column(String)
    created = Column(DateTime, default=datetime.datetime.now)
    email_confirmed = Column(Boolean, nullable=False, default=False)
    is_super_user = Column(Boolean, nullable=False, default=False)
    first_name = Column(String)
    last_name = Column(String)

# coding=utf-8
from pyramidcourse.data.account import Account
from pyramidcourse.data.dbsession import DbSessionFactory
from passlib.handlers.sha2_crypt import sha512_crypt


class AccountService:
    @staticmethod
    def create_account(email, plain_password):
        session = DbSessionFactory.create_session_usr()

        account = Account()
        account.email = email.strip().lower()
        account.password_hash = AccountService.hash_text(plain_password)

        session.add(account)
        session.commit()

        return account

    @classmethod
    def update_account_name(cls, usr_id, first_name, last_name):
        session = DbSessionFactory.create_session_usr()

        account = session.query(Account).get(usr_id)

        account.first_name = first_name.strip()
        account.last_name = last_name.strip()

        session.add(account)
        session.commit()

        return account

    @classmethod
    def find_account_by_email(cls, email):
        if not email.strip():
            return None

        email = email.strip().lower()

        session = DbSessionFactory.create_session_usr()

        account = session.query(Account).filter(Account.email == email).first()

        return account

    @classmethod
    def find_account_by_id(cls, usr_id):
        if not usr_id.strip():
            return None

        session = DbSessionFactory.create_session_usr()

        account = session.query(Account).get(usr_id)

        return account

    @staticmethod
    def hash_text(plain_password):
        hashed_text = sha512_crypt.encrypt(plain_password, rounds=150000)
        return hashed_text

    @classmethod
    def get_authenticated_account(cls, email, plain_password):
        account = AccountService.find_account_by_email(email)
        if not account:
            return None
        if not sha512_crypt.verify(plain_password, account.password_hash):
            return None

        return account

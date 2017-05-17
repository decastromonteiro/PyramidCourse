# coding=utf-8
import hashlib

from datetime import timedelta

auth_cookie_name = 'pyramidcourse_user'


def set_auth(request, user_id):
    hash_val = __hash_text(user_id)
    val = "{}:{}".format(user_id, hash_val)

    request.add_response_callback(lambda req, resp: __add_cookie_callback(
        req, resp, auth_cookie_name, val
    ))


def logout(request):
    request.add_response_callback(lambda req, resp: __delete_cookie_callback(
        resp, auth_cookie_name
    ))


def get_user_id_via_auth_cookie(request):
    if auth_cookie_name not in request.cookies:
        return None

    val = request.cookies[auth_cookie_name]
    parts = val.split(':')

    if len(parts) != 2:
        return None

    user_id = parts[0]
    hash_val = parts[1]

    hash_val_check = __hash_text(user_id)

    if hash_val != hash_val_check:
        print("Warning: Hash mismatch, invalid cookie value")
        return None

    return user_id


def __hash_text(text):
    text = 'a_little_more_salt' + text + '_for_the_text'
    return hashlib.sha512(text.encode()).hexdigest()


def __hash_validate(text):
    return hashlib.sha512(text.encode()).hexdigest()


def __add_cookie_callback(_, response, name, value):
    response.set_cookie(name, value, max_age=timedelta(days=30))


def __delete_cookie_callback(response, name):
    response.delete_cookie(name)

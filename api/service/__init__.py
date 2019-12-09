from api.service.passwd_validator import is_valid
from api.service.login_validator import find_login
from api.service.repository import update_file


def add_user(name, login, password):
    """function for adding new user login"""
    if find_login(login):
        response = "Login already informed", 400
    else:
        pwd = is_valid(password)
        if pwd:
            update_file(f'ADD "{name}", "{login}", "{pwd}"')
            response = "User set to be created", 202
        else:
            response = "Invalid format password!", 400

    return response


def disable_user(login):
    """function for disable user login"""
    if find_login(login):
        response = "Login already informed", 400
    else:
        update_file(f'DISABLE "{login}"')
        response = "Login set to be disabled", 202

    return response

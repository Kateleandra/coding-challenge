from passwd_validator import is_valid
from login_validator import find_login
from Repository import update_file


def add_user(name, login, password):
    if find_login(login):
        return "Login already informed"
    else:
        pwd = is_valid(password)
        if pwd:
            update_file(f'ADD "{name}", "{login}", "{pwd}"')
            return "user set to be created"
        else:
            return "invalid format password!"


def disable_user(login):
    if find_login(login):
        return "Login already informed"
    else:
        update_file(f'DISABLE "{login}"')
        return f"set to be disabled"


if __name__ == "__main__":
    print(add_user("Carla Alves Souza", "carla.souza", "U3Vwb3J0ZTEyMw=="))
    print(add_user("Mateus Santos Lima", "mateus.lima1", "QWJjZDIzNEowMQ=="))
    print(add_user("Mateus Santos Lima", "mateus.lima2", "QWJjZDIzN"))
    print(disable_user("martim.ferreira"))

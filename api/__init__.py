from flask import Flask, request
from api.service import add_user, disable_user


APP = Flask(__name__)


@APP.route("/")
def hello():
    """Testing endpoint for API"""
    return "Hello, World!"


@APP.route("/user", methods=["POST", "DELETE"])
def user_mod():
    """/user route is a both POST and DELETE endpoint for updating user"""
    try:
        missing_param = False

        login = request.get_json()["login"]
        if not login:
            missing_param = True

        if request.method == "POST":
            name = request.get_json()["name"]
            password = request.get_json()["password"]
            if not name or not login or not password:
                missing_param = True

        if missing_param:
            return ("empty parameter values are not allowed", 400)
    except KeyError:
        return ("malformed request syntax", 400)

    if request.method == "POST":
        return add_user(name, login, password)

    if request.method == "DELETE":
        return disable_user(login)

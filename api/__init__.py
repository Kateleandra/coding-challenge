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
    if request.method == "POST":
        try:
            name = request.get_json()["name"]
            login = request.get_json()["login"]
            password = request.get_json()["password"]
            return add_user(name, login, password)
        except KeyError:
            return ("malformed request syntax", 400)

    if request.method == "DELETE":
        try:
            login = request.get_json()["login"]
            return disable_user(login)
        except KeyError:
            return ("malformed request syntax", 400)

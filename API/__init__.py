from flask import Flask, request
from API.Service import add_user, disable_user

app = Flask(__name__)


@app.route("/")
def hello():
    return "Hello, World!"


@app.route("/user", methods=["POST", "DELETE"])
def user_mod():
    if request.method == "POST":
        try:
            name = request.get_json()["name"]
            login = request.get_json()["login"]
            password = request.get_json()["password"]
            return add_user(name, login, password)
        except KeyError:
            return "malformed request syntax", 400

    if request.method == "DELETE":
        try:
            login = request.get_json()["login"]
            return disable_user(login)
        except KeyError:
            return "malformed request syntax", 400

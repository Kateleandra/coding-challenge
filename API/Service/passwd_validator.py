import re
from base64 import b64decode


def decode(pwd):
    try:
        return str(b64decode(pwd))[2:-1]
    except:
        return ""


def is_valid(password: str) -> bool:
    """validates if password has:
    \t 10 characters long
    \t Has 1 Uppercase letter
    \t Has 1 lowercase
    \t Has 1 number"""
    regex = r"^(?=.*[A-Z])(?=.*[a-z])(?=.*[0-9])(?=.{10,})"

    password = decode(password)

    return password if re.match(regex, password) else ""

import re


def is_valid(password: str) -> bool:
    """validates if password has:
    \t 10 characters long
    \t Has 1 Uppercase letter
    \t Has 1 lowercase
    \t Has 1 number"""
    regex = r"^(?=.*[A-Z])(?=.*[a-z])(?=.*[0-9])(?=.{10,})"

    if re.match(regex, password):
        return True
    else:
        return False

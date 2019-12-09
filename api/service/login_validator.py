from api.service.repository import read_file


def get_users() -> dict:
    """Return all users from current file"""
    file_content = read_file()
    users = {}

    for line in file_content:
        if "ADD" in line:
            lgn = line.split(", ")[1][1:-1]
            users[lgn] = "ADD"
        else:
            lgn = line.split("DISABLE ")[1][1:-2]
            users[lgn] = "DISABLE"

    return users


def find_login(login: str) -> bool:
    """Find a user login in current file"""
    user_dict = get_users()

    return bool(login in user_dict.keys())

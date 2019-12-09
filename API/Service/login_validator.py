from Repository import update_file, read_file


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

    return True if login in user_dict.keys() else False

    # TODO: uncomment if find to enable only users
    # if login in user_dict.keys():
    #     if user_dict[login] == "ADD":
    #         return True

    # return False

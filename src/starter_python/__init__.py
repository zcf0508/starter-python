import getpass


def hello():
    username = getpass.getuser()
    return f"Hello `{username}` from starter-python!"

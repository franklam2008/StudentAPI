import jwt
from data.keys import JWT_KEY


def found_user(each, email, pw):
    if each["email"] == email and each["password"] == pw:
        return True
    else:
        return False


def check_required_cap(cap, token):
    if not token:
        return "User is not Logged in"

    foundUser = jwt.decode(token, JWT_KEY, algorithms="HS256")
    caps = foundUser['capabilities']
    if not cap in caps:
        return "User does not have permissions"

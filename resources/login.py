import jwt
from flask_restful import Resource
from flask import request
from data.user_details import USER_DETAILS
from data.user_logins import USER_LOGINS

# JWT authentication
# =================================================

key = "SUPER_TEST_SECRET"

# Find users with input


class Login(Resource):
    def put(self):
        foundUser = {}
        name = request.args.get('username')
        pw = request.args.get('password')
        for each in USER_LOGINS:
            if found_user(each, name, pw):
                foundId = each["uuid"]
                found_detail = USER_DETAILS[foundId]
                encoded = jwt.encode(found_detail, key, algorithm="HS256")
                foundUser = jwt.decode(encoded, key, algorithms="HS256")
                break

        # PUT call Response

        if foundUser:
            return foundUser, 200
        else:
            return "", 404


def found_user(each, name, pw):
    if each["username"] == name and each["password"] == pw:
        return True
    else:
        return False

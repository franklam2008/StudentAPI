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
    def post(self):
        foundUser = {}
        name = request.args.get('username')
        pw = request.args.get('password')
        for each in USER_LOGINS:
            if found_user(each, name, pw):
                foundId = each["uuid"]
                foundUser = USER_DETAILS[foundId]
                encoded = jwt.encode(foundUser, key, algorithm="HS256")
                break

        # PUT call Response

        if foundUser:
            foundUser['jwt'] = encoded
            return foundUser, 200
        else:
            return "", 404

    # GET user detail from token
    def get(self):
        foundUser = {}
        jwt_from_cookie = request.args.get('jwt')
        if jwt_from_cookie:
            foundUser = jwt.decode(jwt_from_cookie, key, algorithms="HS256")

        if foundUser:
            return foundUser, 200
        else:
            return "", 404


def found_user(each, name, pw):
    if each["username"] == name and each["password"] == pw:
        return True
    else:
        return False

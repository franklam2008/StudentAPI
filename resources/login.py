import jwt
from flask_restful import Resource
from flask import after_this_request, request
from data.user_details import USER_DETAILS
from data.user_logins import USER_LOGINS

# JWT authentication
# =================================================

key = "SUPER_TEST_SECRET"

# Find users with input


class Login(Resource):
    def post(self):
        foundUser = {}
        email = request.args.get('email')
        pw = request.args.get('password')
        for each in USER_LOGINS:
            if found_user(each, email, pw):
                foundId = each["uuid"]
                foundUser = USER_DETAILS[foundId]
                encoded = jwt.encode(foundUser, key, algorithm="HS256")
                break

        # PUT call Response

        if foundUser:
            foundUser['jwt'] = encoded
       
            # PUT call add Cookies
            @after_this_request
            def set_cookie_value(response):
                response.set_cookie('ENCODED_TOKEN', str(
                    encoded), max_age=44, httponly=True)
                response.set_cookie('USERNAME', str(
                    foundUser['username']), max_age=44, httponly=True)
                return response

            return foundUser, 200
        else:
            return "", 404

    # GET user detail from token
    def get(self):
        foundUser = {}
        token = request.cookies.get('ENCODED_TOKEN')

        if token:
            foundUser = jwt.decode(token, key, algorithms="HS256")

        if foundUser:
            return foundUser, 200
        else:
            return "Token not found, User is not logged in", 404


def found_user(each, email, pw):
    if each["email"] == email and each["password"] == pw:
        return True
    else:
        return False

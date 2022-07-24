import jwt
from flask_restful import Resource
from flask import after_this_request, request
from data.user_details import USER_DETAILS
from data.user_logins import USER_LOGINS
from resources.helpers.helpers import found_user
# from dotenv import dotenv_values


# JWT authentication
# =================================================

# config = dotenv_values(".env")
# JWT_KEY = config['JWT_KEY']
JWT_KEY = 'SUPER_JWT_SECREY_KEY_GSEGAWDAFAWF'
COOKIES_AGE = 60 * 60 * 1000

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
                encoded = jwt.encode(foundUser, JWT_KEY, algorithm="HS256")

                # decode bytes to string for pythonanywhere
                # =================================================
                if isinstance(encoded, bytes):
                    encoded = encoded.decode('utf-8')

                break

        # PUT call Response

        if foundUser:

            # Set Cookies for response header
            @after_this_request
            def set_cookie_value(response):
                response.set_cookie('ENCODED_TOKEN', str(
                    encoded), max_age=COOKIES_AGE, httponly=True)
                response.set_cookie('USERNAME', str(
                    foundUser['username']), max_age=COOKIES_AGE, httponly=True)
                return response

            return {'message': 'login success'}, 200
        else:
             # Remove Cookies if user not found
            @after_this_request
            def set_cookie_value(response):
                response.set_cookie('ENCODED_TOKEN', '', expires=0)
                response.set_cookie('USERNAME', '', expires=0)
                return response
          
            return "", 404

    # GET user detail from token
    def get(self):
        foundUser = {}
        token = request.cookies.get('ENCODED_TOKEN')

        if token:
            foundUser = jwt.decode(token, JWT_KEY, algorithms="HS256")

        if foundUser:
            return foundUser, 200
        else:
            return "Token not found, User is not logged in", 404

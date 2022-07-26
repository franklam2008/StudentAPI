import jwt
from flask_restful import Resource
from flask import request
from data.keys import JWT_KEY



class Whoami(Resource):

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

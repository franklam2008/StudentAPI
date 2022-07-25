
from flask import request
from flask_restful import Resource
from data.students import STUDENTS
from resources.helpers.helpers import check_required_cap


class StudentsList(Resource):
    def get(self):
        # error = check_required_cap(
        #     "VIEW",  request.cookies.get('ENCODED_TOKEN'))
        # if error:
        #     return error, 404

        return STUDENTS, 200

    def post(self):
        error = check_required_cap(
            "CREATE", request.cookies.get('ENCODED_TOKEN'))
        if error:
            return error, 404

        name = request.args.get('name')
        age = request.args.get('age')
        spec = request.args.get('spec')

        student_id = int(max(STUDENTS.keys())) + 1
        student_id = '%i' % student_id

        if name and age and spec:
            STUDENTS[student_id] = {
                "name": name,
                "age": age,
                "spec": spec,
            }
            return STUDENTS[student_id], 201
        else:
            return "Args ERROR", 404

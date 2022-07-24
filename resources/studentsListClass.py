
from flask import Flask, request
from flask_restful import Resource, Api
from data.studentsData import STUDENTS

class StudentsList(Resource):
    def get(self):
        return STUDENTS

    def post(self):
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


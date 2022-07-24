
from flask import Flask, request
from flask_restful import Resource, Api
from data.students import STUDENTS


class Student(Resource):
    def get(self, student_id):
        if student_id not in STUDENTS:
            return "Not found", 404
        else:
            return STUDENTS[student_id]

    def put(self, student_id):
        name = request.args.get('name')
        age = request.args.get('age')
        spec = request.args.get('spec')
        if student_id not in STUDENTS:
            return "Record not found", 404
        else:
            student = STUDENTS[student_id]
            student["name"] = name if name is not None else student["name"]
            student["age"] = age if age is not None else student["age"]
            student["spec"] = spec if spec is not None else student["spec"]
            return student, 200

    def delete(self, student_id):
        if student_id not in STUDENTS:
            return "Not found", 404
        else:
            del STUDENTS[student_id]
            return '', 204

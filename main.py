from flask import Flask, request
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)

# mock students list

STUDENTS = {
    '1': {'name': 'Mark', 'age': 23, 'spec': 'math'},
    '2': {'name': 'Jane', 'age': 20, 'spec': 'biology'},
    '3': {'name': 'Peter', 'age': 21, 'spec': 'history'},
    '4': {'name': 'Kate', 'age': 22, 'spec': 'science'},
    '5': {'name': 'John', 'age': 42, 'spec': 'Spanish'},
}

# student list


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


api.add_resource(StudentsList, '/students/')
api.add_resource(Student, '/students/<student_id>')


if __name__ == "__main__":
    app.run(debug=True)

from flask import Flask
from flask_restful import Api
from flask_cors import CORS
# Resources
from resources.login import Login
from resources.studentClass import Student
from resources.studentsListClass import StudentsList

app = Flask(__name__)
CORS(app)
api = Api(app)

# Add classes
# =================================================

api.add_resource(Login, '/login/')
api.add_resource(StudentsList, '/students/')
api.add_resource(Student, '/students/<student_id>')


if __name__ == "__main__":
    app.run(debug=True)

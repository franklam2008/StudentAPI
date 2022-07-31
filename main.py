from flask import Flask
from flask_restful import Api
from flask_cors import CORS
# Resources
from resources.login import Login
from resources.studentClass import Student
from resources.studentsListClass import StudentsList
from resources.whoami import Whoami

cors_config = {
    'origins': ['http://127.0.0.1:5173', 'http://localhost:5173'],
    'methods': ["OPTIONS", "GET", "POST", "DELETE"],
    'allow_headers': ['Authorization', 'Content-Type'],
    'supports_credentials': True,
}

app = Flask(__name__)
cors = CORS(app, resources={r'*': cors_config})
api = Api(app)

# Add Resources
# =================================================

api.add_resource(Login, '/login/')
api.add_resource(StudentsList, '/students/')
api.add_resource(Student, '/students/<student_id>')
api.add_resource(Whoami, '/whoami')


if __name__ == "__main__":
    app.run(debug=True)

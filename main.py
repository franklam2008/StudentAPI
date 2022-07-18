from flask import Flask, request
from flask_restful import Resource, Api

from studentClass import Student
from studentsData import STUDENTS
from studentsListClass import StudentsList

app = Flask(__name__)
api = Api(app)

api.add_resource(StudentsList, '/students/')
api.add_resource(Student, '/students/<student_id>')


if __name__ == "__main__":
    app.run(debug=True)




# import mysql.connector
# mydb = mysql.connector.connect(
#     host="franklam2008.mysql.pythonanywhere-services.com",
#     user="franklam2008",
#     password="qQ_6RdzCfDkg@@_"
# )

# if(mydb):
#     print("mydb", mydb)
# else:
#     print('mydb undefined')

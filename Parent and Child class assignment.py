# Creating class "user" for the school to provide logins
class user:
    name = ''
    grade = ''
    password = ''
    Id_Number = ''
# Child class "teacher" to give teacher its own attributes for salary and class number
class Teacher(user):
    Salary = 23.50
    Homeroom = 416
# Child class "Student" to give student its own attributes for GPA and expected graduation date
class Student(user):
    GPA = 3.7
    Expected Graduation = 2022

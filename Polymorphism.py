#Parent Class User
class User:
    name = "James"
    email = "jamesw1323@gmail.com"
    password = "Password123"

    def getLoginInfo(self):
        entry_name = input("Please enter your name: ")
        entry_email = input("Please enter your email: ")
        entry_password = input("Please enter your password: ")
        if (entry_email == self.email and entry_password == self.password):
            print("Welcome back, {}!".format(entry_name))
        else:
            print("The Password you entered is incorrecy.")

#Child Class Employee
class Employee(User):
    base_pay = 11.00
    department = "General"
    pin_number = "3980"

# This is the same method in the parent class "user".
#The difference is that, instead of using password, we're using pin.

    def getLoginInfo(self):
        entry_name = input("Enter your name: ")
        entry_email = input("Enter your email: ")
        entry_pin = input("Enter your pin: ")
        if (entry_email == self.email and entry_pin == self.pin_number):
            print("Welcom back, {}!".format(entry_name))
        else:
            print("The pin is invalid")

#Child Class student
class Student(User):
    Grade = 12
    department = "General"
    student_number = "5454"

# This is the same method in the parent class "user".
#The difference is that, instead of using password or pin, we are using student ID

    def getLoginInfo(self):
        entry_name = input("Enter your name: ")
        entry_email = input("Enter your email: ")
        entry_ID = input("Enter your student ID: ")
        if (entry_email == self.email and entry_ID == self.student_number):
            print("Welcom back, {}!".format(entry_name))
        else:
            print("The ID is invalid")



#The following code invokes the methods inside each class for user and employee

customer = User()
customer.getLoginInfo()

manager = Employee()
manager.getLoginInfo()

student = Student()
student.getLoginInfo()

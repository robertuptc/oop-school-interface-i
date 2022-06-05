from classes.school import School
from classes.student import Student
from classes.staff import Staff

school = School('Ridfemont High')
print(school.name)

# michael = Student('Michael', 34, 'Student', '0001', "mypassword2022")
# print(michael.role)

# karen = Staff('Karen', 55, 'Staff', '0002', "oldpassword2022")
# print(karen.name)


# student_info = {'name' : 'Diana', 'password' : 'password', 'school_id' : 12345, 'age' : 17, 'role' : 'Student'}
# diana = Student(**student_info)
# print(diana.name, diana.password, diana.role)

# Student.all_students()
print(school.staff)
print(school.students)
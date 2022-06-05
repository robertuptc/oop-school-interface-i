from classes.person import Person
import csv

class Student(Person):
    def __init__(self, name, age, role, school_id, password):
        super().__init__(name, age, role, password)
        self.school_id = school_id

    def all_students():
        students_list = []
        with open(f"/Users/robert/Exercises/oop-school-interface-i/data/students.csv") as f:
            students_reader = csv.DictReader(f)
            for row in students_reader:
                students_list.append(Student(**row))
            return students_list









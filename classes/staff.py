from classes.person import Person
import csv

class Staff(Person):
    def __init__(self, name, age, role, employee_id, password):
        super().__init__(name, age, role, password)
        self.employee_id = employee_id

    def all_staff():
        staff_list = []
        with open(f"/Users/robert/Exercises/oop-school-interface-i/data/staff.csv") as f:
            staff_reader = csv.DictReader(f)
            for row in staff_reader:
                staff_list.append(Staff(**row))
            return staff_list














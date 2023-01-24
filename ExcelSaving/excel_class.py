import csv
import os
class ExcelStudend:
    def __init__(self, fullname: str, age: int,
                 school: str, phone_number: str, photo: str, email: str, family: str, mom_number: str,
                 dad_number: str, mom_work: str, dad_work: str):
        self.fullname = fullname
        self.age = age
        self.school = school
        self.phone_number = phone_number
        self.photo = photo
        self.email = email
        self.family = family
        self.mom_number = mom_number
        self.dad_number = dad_number
        self.mom_work = mom_work
        self.dad_work = dad_work
    def run(self):
        if os.stat("data/students.csv").st_size == 0:
            ExcelStudend.add_columns_name(self)
        ExcelStudend.add_main_information(self)
    def add_main_information(self):
        with open('data/students.csv', 'a', newline='') as file:
            writer = csv.writer(file, delimiter=',')
            writer.writerow([self.fullname, self.age, self.school, self.phone_number, self.photo, self.email,
                             self.family, self.mom_number, self.dad_number, self.mom_work, self.dad_work])
    def add_columns_name(self):
        with open('data/students.csv', 'a', newline='') as file:
            writer = csv.writer(file, delimiter=',')
            writer.writerow(["Full name", "Age", "School", "Mobile phone", "Path to photo", "Email",
                             "Family","Mom's number", "Dad's number", "Mom's work", "Dad's work"])


excel = ExcelStudend('sfs', 3, 'sdf', 'sdf', 'sdf', 'sdf', 'sdf', 'sdf', 'sdf', 'sdf', 'sdf')
excel.run()
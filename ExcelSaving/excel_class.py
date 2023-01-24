import csv
import os
class ExcelStudend:


    def __init__(self, fullname: str, age: int,
                 school: str, phone_number: str, photo: str, email: str, family: str, mom_number: str,
                 dad_number: str, mom_work: str, dad_work: str, floor: str, group: str):
        '''
        Иницилизация класса
        :param fullname: str
        :param age: int
        :param school: str
        :param phone_number: str
        :param photo: str
        :param email: str
        :param family: str
        :param mom_number: str
        :param dad_number: str
        :param mom_work: str
        :param dad_work: str
        :param floor: str
        :param group: str
        '''
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
        self.floor = floor
        self.group = group


    def __repr__(self):
        '''
        Вызываеться при выводе экземпляра
        :return: str
        '''
        return '''Принимает в себя 13 элементов: 
        ФИО
        Возраст
        Школу
        Номер телефона
        Путь на фотку
        Почту
        Состав семьи
        Мамин номер телефона
        Папин номер телефона
        Работа мамы
        Работа папы
        Пол
        Группа
        '''


    def run(self):
        '''
        Главная функция посредством котоорой запускаеться весь класс
        :return:
        '''
        if os.stat("data/students.csv").st_size == 0:
            ExcelStudend.add_columns_name(self)
        ExcelStudend.add_main_information(self)


    def add_main_information(self):
        '''
        Записывает/дозаписывает в данные в таблицу
        :return:
        '''
        with open('data/students.csv', 'a', newline='') as file:
            writer = csv.writer(file, delimiter=',')
            writer.writerow([self.fullname, self.age, self.school, self.phone_number, self.photo, self.email,
                             self.family, self.mom_number, self.dad_number, self.mom_work, self.dad_work, self.floor,
                             self.group])


    def add_columns_name(self):
        '''
        Добавление названий таблицы
        :return:
        '''
        with open('data/students.csv', 'a', newline='') as file:
            writer = csv.writer(file, delimiter=',')
            writer.writerow(["Full name", "Age", "School", "Mobile phone", "Path to photo", "Email",
                             "Family","Mom's number", "Dad's number", "Mom's work", "Dad's work", "Floor", "Group"])
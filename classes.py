
class Person:
    """
    Ushbu klass foydalanuchining ism, familiya, tugulgan yili ha hokazo malumotlarni ozida
    saqlaydi da Student Admin klasslariga super klass hisoblanadi
    """
    def __init__(self, name, surname, birth_year, phone_number, username, password):
        self.name = name
        self.surname = surname
        self.birth_year = birth_year
        self.__phone_number = phone_number
        self.__username = username
        self.__password = password

    def get_fullname(self):
        return f"{self.name} {self.surname}"

    def get_fullinfo(self):
        return f"Ism: {self.name}, Familiya: {self.surname}," \
               f" Tug'ulgan yilim: {self.birth_year}" \
               f"Tel. raqamim: {self.__phone_number}"

    def get_password(self):
        return f"Parol: {self.__password}" \
               f"Username: {self.__username}"




class Student(Person):
    def __init__(self, name, surname, birth_year, phone_number, username, password,
                 courses, group, payment):
        Person.__init__(self, name, surname, birth_year, phone_number, username, password)
        self.courses = courses
        self.group = group
        self.payment =  payment

    def get_fullname(self):
        return f"{self.name} {self.surname}"

    def get_fullinfo(self):
        return f"Ism: {self.name}, Familiya: {self.surname}," \
               f" Tug'ulgan yilim: {self.birth_year}" \
               f"Tel. raqamim: {self.__phone_number}" \
               f"Kurslarim: {self.courses}, Tolovlarim: {self.payment}"


    def get_courses(self):
        return f"Siz {self.courses} kursida o'qiysiz"

    def get_payment(self):
        return self.payment

    def get_group_info(self):
        return f"Sizning guruhingiz: {self.group}"

class Teacher(Person):
    def __init__(self, name, surname, birth_year, phone_number, username, password)
        Person.__init__(self, name, surname, birth_year, phone_number, username, password)

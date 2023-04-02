from datetime import datetime
class Person:
    # данный метод описывет person :
    # возвращает имя,
    # на основе года рождения рассчитывает возраст,
    # person может вступать в брак с другими persons
    def __init__(self, name, year_of_birth, age=0, city="Saint_Petersburg", is_married_to=None, sex="жен"):
        self.name = name
        self.year_of_birth = year_of_birth
        self.age = int(datetime.now().year)- int(year_of_birth)
        self.city = city
        self.is_married_to = is_married_to
        self.sex = sex

    def introduce_yourself(self):
        print(f"Здравствуйте, меня зовут {self.name}")

    def age_person(self):
        print(f"Мне {self.age}")

    def wedding(self, other_person):
        if other_person.age < 18:
            print(f"{self.name},Ваш избранник {other_person.name} не достиг совершеннолетия")
        elif self.age < 18:
            print(f"{self.name},Вы не достигли совершеннолетия")
        elif self.sex == other_person.sex:
            print(f"К сожалению,{self.name}, ваши отношения c {other_person.name} невозможно оформить в России")
        elif self.is_married_to is not None:
            print(f"{self.name},чтобы повторно вступить в брак, нужно развестись с {self.is_married_to}")
        else:
            self.is_married_to = other_person.name
            other_person.wedding(self)
            print(f"{self.name}, поздравляю, вы поженились")
            self.is_married(self.is_married_to)

    def is_married(self, is_married_to):
        if self.is_married_to == None:
            print("Не состоит в браке")

            return ("Не состоит в браке")
        else:
            return (f"{self.name} состоит в браке с {is_married_to}")

    def city_from(self):
        print(f"Я из города {self.city}")

class Student(Person):
    # дочерний класс от Person, содержит год поступления в школу, средний балл и год выпуска
    def __init__(self, name, year_of_birth, school, admission_year, graduation_year, gpa, age=0, city="Saint_Petersburg", is_married_to=None, sex="жен"):
        super().__init__(name, year_of_birth, age, city, is_married_to, sex)
        self.school = school
        self.admission_year = admission_year
        self.graduation_year = graduation_year
        self.gpa = gpa

    def attend_school(self,sex):
        if self.admission_year is not None:
            if self.sex=="жен":
                print(f"{self.name} поступила в {self.school} в {self.admission_year} году")
            else:
                print(f"{self.name} поступил в {self.school} в {self.admission_year} году")
        else:
            print(f"{self.name} еще не учится в школе")

    def graduate(self):
        if self.graduation_year is not None:
            print(f"{self.name} выпустился из {self.school} в {self.graduation_year} году.Средний балл {self.gpa}")
        elif self.admission_year is not None:
            print(f"{self.name} еще обучается в {self.school} ")
        else:
            print(f"{self.name} еще не учится в школе")



students=[]
students.append(Student(name="Иван", year_of_birth=2002, school="Школа №123", admission_year= 2016, graduation_year= 2020, gpa=3.0))
students.append(Student(name="Ира", year_of_birth=1990, school="Школа №250", admission_year= 2018, graduation_year= 2022, gpa=4.5))
students.append(Student(name="Ира", year_of_birth=1990, school="Школа №250", admission_year= None, graduation_year= None, gpa=None))
students.append(Student(name="Ира", year_of_birth=1990, school="Школа №250", admission_year= 2023, graduation_year= None, gpa=None))





persons = []
persons.append(Person(name="Маша", year_of_birth=1992, sex="жен"))
persons.append(Person(name="Дима", year_of_birth=1984, sex="муж"))
persons.append(Person(name="Петя", year_of_birth=2020, sex="муж"))
persons.append(Person(name="Вася", year_of_birth=1990, sex="муж"))

persons[0].wedding(students[1])
persons[1].wedding(students[1])
persons[1].wedding(persons[0])
persons[2].wedding(persons[3])

for person in persons:
    person.introduce_yourself()
    person.age_person()
    person.city_from()
    person.is_married(person.is_married_to)

for student in students:
    student.introduce_yourself()
    student.age_person()
    student.city_from()
    person.is_married(person.is_married_to)
    student.attend_school(student.sex)
    student.graduate()

for index, s in enumerate(students):
    print(f" {index} Имя={s.name},год рождения ={s.year_of_birth}, школа={s.school}, год поступления={s.admission_year}, год окончания ={s.graduation_year}, средний балл={s.gpa}, город ={s.city}, в браке с {s.is_married_to},пол={s.sex}")

for index, s in enumerate(persons):
    print(f" {index} Имя={s.name},год рождения ={s.year_of_birth}, город ={s.city}, в браке с {s.is_married_to},пол={s.sex}")




from abc import ABC, abstractmethod


class PrivateSchool:
    def __init__(self, name):
        self.name = name
        self.teachers = []
        self.school_classes = []
        self.headteachers = []
        self.director = []
        self.pupils = []

    def get_teachers(self):
        teachers_fullname = []
        for i in self.teachers:
            teachers_fullname.append(f"{i.name} {i.surname}")
        return teachers_fullname

    def school_salary_calculate(self):
        full_personal_salary = 0
        for i in self.headteachers:
            full_personal_salary += i.salary
        for i in self.teachers:
            full_personal_salary += i.salary
        for i in self.director:
            full_personal_salary += i.salary
        return full_personal_salary

    def one_pupil_payment(self):
        one_pupil = self.school_salary_calculate() // len(self.pupils)
        return one_pupil

    def pupil_payment_profit(self, profit_value):
        profit_one_pupil = (self.school_salary_calculate() + profit_value) // len(self.pupils)
        return profit_one_pupil

    def get_avg_mark(self):
        fully_marks = 0
        marks_numbers = 0
        for i in self.pupils:
            marks_numbers += len(i.marks)
            for a in i.marks:
                fully_marks += a
        avg_mark = fully_marks / marks_numbers if fully_marks != 0 else 0
        return avg_mark


class SchoolClass:
    def __init__(self, name, school, teacher):
        self.school = school
        self.name = name
        self.teacher = teacher
        self.pupils = []
        self.marks = []
        school.school_classes.append(self.name)

    def deleting(self):
        self.pupils = []
        self.teacher = None
        self.school.school_classes.remove(self.name)
        self.school = None
        return f"The {self.name} class deleted from school"

    def get_pupils(self):
        return self.pupils

    def get_avg_mark(self):
        fully_marks = 0
        for i in self.marks:
            fully_marks += i
        avg_mark = fully_marks / len(self.marks) if fully_marks != 0 else 0
        return avg_mark


class Staff(ABC):
    def __init__(self, name, surname, age, school):
        self.name = name
        self.surname = surname
        self.age = age
        self.school = school

    @abstractmethod
    def get_salary(self):
        pass


class Teacher(Staff):

    def __init__(self, name, surname, age, school):
        super().__init__(name, surname, age, school)
        self.salary = 6000
        school.teachers.append(self)

    @staticmethod
    def add_marks(pupil, marks):
        if pupil.school_class is None:
            return f"The {pupil.name} {pupil.surname} not included in the class"
        else:
            pupil.marks.append(marks)
            pupil.school_class.marks.append(marks)
            return f"The {marks} mark added for the {pupil.name} {pupil.surname}"

    def get_salary(self):
        return f"The {self.salary} received on the card"


class Director(Staff):
    def __init__(self, name, surname, age, school):
        super().__init__(name, surname, age, school)
        school.director.append(self)
        self.salary = 20000

    @staticmethod
    def invite_new_pupil(school_class, pupil):
        school_class.pupils.append(f"{pupil.name} {pupil.surname}")
        pupil.school_class = school_class
        return f"{pupil.name} {pupil.surname} is new student in the class"

    @staticmethod
    def fire_pupil(school_class, pupil):
        school_class.pupils.remove(f"{pupil.name} {pupil.surname}")
        return f"{pupil.name} {pupil.surname} fired from the school"

    @staticmethod
    def invite_new_teacher(school, teacher):
        school.teachers.append(f"{teacher.name} {teacher.surname}")
        return f"{teacher.name} {teacher.surname} is new teacher in the school"

    @staticmethod
    def fire_teacher(school, teacher):
        school.teachers.remove(f"{teacher.name} {teacher.surname}")
        return f"{teacher.name} {teacher.surname} fired from the school"

    @staticmethod
    def invite_new_headteacher(school, headteachers):
        school.headteachers.append(f"{headteachers.name} {headteachers.surname}")
        return f"{headteachers.name} {headteachers.surname} is new headteacher of school"

    @staticmethod
    def fire_headteachers(school, headteachers):
        school.headteachers.remove(f"{headteachers.name} {headteachers.surname}")
        return f"{headteachers.name} {headteachers.surname} fired from the school"

    def get_salary(self):
        return f"The {self.salary} received on the card"


class HeadTeacher(Staff):

    def __init__(self, name, surname, age, school):
        super().__init__(name, surname, age, school)
        self.salary = 15000
        school.headteachers.append(self)

    def get_salary(self):
        return f"The {self.salary} received on the card"


class Pupil(Staff):
    def __init__(self, name, surname, age, school):
        super().__init__(name, surname, age, school)
        school.pupils.append(self)
        self.school_class = None
        self.marks = []

    def get_avg_mark(self):
        full_marks = 0
        for i in self.marks:
            full_marks += i
        avg_mark = full_marks / len(self.marks) if full_marks != 0 else 0
        return avg_mark

    def get_salary(self):
        return f"The {self.marks} marks received in the school"


school_1 = PrivateSchool("Hunt school")
director_of_school = Director("Dean", "Winchester", 22, school_1)
teacher_1 = Teacher("Serena", "Watts", 22, school_1)
teacher_2 = Teacher("Glenn", "Haley", 21, school_1)
headteacher_1 = HeadTeacher("Evangeline", "Lester", 32, school_1)
pupil_1 = Pupil("Tamara", "Hickman", 22, school_1)
pupil_2 = Pupil("Rogelio", "Gibson", 20, school_1)
pupil_3 = Pupil("Sandra", "Cardenas", 21, school_1)
cls1 = SchoolClass("11-A", school_1, teacher_1)
cls2 = SchoolClass("7-B", school_1, teacher_2)
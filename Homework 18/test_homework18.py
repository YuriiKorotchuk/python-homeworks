import Homework18
import datetime
import pytest


@pytest.fixture
def new_school():
    return Homework18.PrivateSchool("Hunt school")


def test_new_director(new_school):
    director_of_school = Homework18.Director("Dean", "Winchester", datetime.date(1985, 8, 11), new_school)
    assert director_of_school.name == "Dean" and director_of_school.surname == "Winchester" and \
           director_of_school.age == (datetime.date.today() - datetime.date(1985, 8, 11)).days // 365


def test_new_headteacher(new_school):
    headteacher_1 = Homework18.HeadTeacher("Evangeline", "Lester", datetime.date(1988, 3, 10), new_school)
    assert headteacher_1.name == "Evangeline" and headteacher_1.surname == "Lester" and \
           headteacher_1.age == (datetime.date.today() - datetime.date(1988, 3, 10)).days // 365


def test_new_teacher(new_school):
    teacher_1 = Homework18.Teacher("Serena", "Watts", datetime.date(1990, 10, 29), new_school)
    assert teacher_1.name == "Serena" and teacher_1.surname == "Watts" and \
           teacher_1.age == (datetime.date.today() - datetime.date(1990, 10, 29)).days // 365


def test_new_pupil(new_school):
    learner_1 = Homework18.Pupil("Tamara", "Hickman", datetime.date(2004, 2, 13), new_school)
    assert learner_1.name == "Tamara" and learner_1.surname == "Hickman" and \
           learner_1.age == (datetime.date.today() - datetime.date(2004, 2, 13)).days // 365


def test_invite_pupil(new_school):
    director_of_school = Homework18.Director("Dean", "Winchester", datetime.date(1985, 8, 11), new_school)
    teacher_1 = Homework18.Teacher("Serena", "Watts", datetime.date(1990, 10, 29), new_school)
    school_class_1 = Homework18.SchoolClass("1-A", new_school, teacher_1)
    learner_1 = Homework18.Pupil("Tamara", "Hickman", datetime.date(2004, 2, 13), new_school)
    learner_2 = Homework18.Pupil("Rogelio", "Gibson", datetime.date(2004, 3, 16), new_school)
    learner_3 = Homework18.Pupil("Sandra", "Cardenas", datetime.date(2005, 5, 23), new_school)
    director_of_school.invite_new_pupil(school_class_1, learner_1)
    director_of_school.invite_new_pupil(school_class_1, learner_2)
    director_of_school.invite_new_pupil(school_class_1, learner_3)
    assert school_class_1.pupils_quantity() == 3


def test_remove_pupil(new_school):
    director_of_school = Homework18.Director("Dean", "Winchester", datetime.date(1985, 8, 11), new_school)
    teacher_1 = Homework18.Teacher("Serena", "Watts", datetime.date(1990, 10, 29), new_school)
    school_class_1 = Homework18.SchoolClass("1-A", new_school, teacher_1)
    learner_1 = Homework18.Pupil("Tamara", "Hickman", datetime.date(2004, 2, 13), new_school)
    learner_2 = Homework18.Pupil("Rogelio", "Gibson", datetime.date(2004, 3, 16), new_school)
    learner_3 = Homework18.Pupil("Sandra", "Cardenas", datetime.date(2005, 5, 23), new_school)
    director_of_school.invite_new_pupil(school_class_1, learner_1)
    director_of_school.invite_new_pupil(school_class_1, learner_2)
    director_of_school.invite_new_pupil(school_class_1, learner_3)
    director_of_school.fire_pupil(school_class_1, learner_2)
    director_of_school.fire_pupil(school_class_1, learner_3)
    assert len(school_class_1.pupils) == 1


def test_learners_quantity(new_school):
    teacher_1 = Homework18.Teacher("Serena", "Watts", datetime.date(1990, 10, 29), new_school)
    school_class_1 = Homework18.SchoolClass("1-A", new_school, teacher_1)
    assert school_class_1.pupils_quantity() == 0


def test_correct_school_fees(new_school):
    director_of_school = Homework18.Director("Dean", "Winchester", datetime.date(1985, 8, 11), new_school)
    headteacher_1 = Homework18.HeadTeacher("Evangeline", "Lester", datetime.date(1988, 3, 10), new_school)
    teacher_1 = Homework18.Teacher("Serena", "Watts", datetime.date(1990, 10, 29), new_school)
    school_class_1 = Homework18.SchoolClass("1-A", new_school, teacher_1)
    learner_1 = Homework18.Pupil("Tamara", "Hickman", datetime.date(2004, 2, 13), new_school)
    director_of_school.invite_new_pupil(school_class_1, learner_1)
    learner_2 = Homework18.Pupil("Rogelio", "Gibson", datetime.date(2004, 3, 16), new_school)
    director_of_school.invite_new_pupil(school_class_1, learner_2)
    assert new_school.one_pupil_payment() == 20500


def test_one_pupil_payment(new_school):
    director_of_school = Homework18.Director("Dean", "Winchester", datetime.date(1985, 8, 11), new_school)
    headteacher_1 = Homework18.HeadTeacher("Evangeline", "Lester", datetime.date(1988, 3, 10), new_school)
    teacher_1 = Homework18.Teacher("Serena", "Watts", datetime.date(1990, 10, 29), new_school)
    school_class_1 = Homework18.SchoolClass("1-A", new_school, teacher_1)
    learner_1 = Homework18.Pupil("Tamara", "Hickman", datetime.date(2004, 2, 13), new_school)
    director_of_school.invite_new_pupil(school_class_1, learner_1)
    learner_2 = Homework18.Pupil("Rogelio", "Gibson", datetime.date(2004, 3, 16), new_school)
    director_of_school.invite_new_pupil(school_class_1, learner_2)
    assert new_school.one_pupil_payment() == 20500
    learner_3 = Homework18.Pupil("Sandra", "Cardenas", datetime.date(2005, 5, 23), new_school)
    director_of_school.invite_new_pupil(school_class_1, learner_3)
    assert new_school.one_pupil_payment() == 13666


def test_improved_pupil_payment(new_school):
    director_of_school = Homework18.Director("Dean", "Winchester", datetime.date(1985, 8, 11), new_school)
    headteacher_1 = Homework18.HeadTeacher("Evangeline", "Lester", datetime.date(1988, 3, 10), new_school)
    teacher_1 = Homework18.Teacher("Serena", "Watts", datetime.date(1990, 10, 29), new_school)
    school_class_1 = Homework18.SchoolClass("1-A", new_school, teacher_1)
    learner_1 = Homework18.Pupil("Tamara", "Hickman", datetime.date(2004, 2, 13), new_school)
    director_of_school.invite_new_pupil(school_class_1, learner_1)
    learner_2 = Homework18.Pupil("Rogelio", "Gibson", datetime.date(2004, 3, 16), new_school)
    director_of_school.invite_new_pupil(school_class_1, learner_2)
    assert new_school.one_pupil_payment() == 20500
    director_of_school.fire_pupil(school_class_1, learner_2)
    new_school.pupils.remove(learner_2)
    assert new_school.one_pupil_payment() == 41000


def test_pupil_dublicated(new_school):
    director_of_school = Homework18.Director("Dean", "Winchester", datetime.date(1985, 8, 11), new_school)
    teacher_1 = Homework18.Teacher("Serena", "Watts", datetime.date(1990, 10, 29), new_school)
    school_class_1 = Homework18.SchoolClass("1-A", new_school, teacher_1)
    learner_1 = Homework18.Pupil("Tamara", "Hickman", datetime.date(2004, 2, 13), new_school)
    director_of_school.invite_new_pupil(school_class_1, learner_1)
    assert director_of_school.invite_new_pupil(school_class_1, learner_1) == "This pupil already in the class"


def test_pupil_avg_mark(new_school):
    director_of_school = Homework18.Director("Dean", "Winchester", datetime.date(1985, 8, 11), new_school)
    teacher_1 = Homework18.Teacher("Serena", "Watts", datetime.date(1990, 10, 29), new_school)
    school_class_1 = Homework18.SchoolClass("1-A", new_school, teacher_1)
    learner_1 = Homework18.Pupil("Tamara", "Hickman", datetime.date(2004, 2, 13), new_school)
    director_of_school.invite_new_pupil(school_class_1, learner_1)
    teacher_1.add_marks(learner_1, 3)
    teacher_1.add_marks(learner_1, 10)
    teacher_1.add_marks(learner_1, 5)
    assert learner_1.get_avg_mark() == 6.0


def test_class_avg_mark(new_school):
    director_of_school = Homework18.Director("Dean", "Winchester", datetime.date(1985, 8, 11), new_school)
    teacher_1 = Homework18.Teacher("Serena", "Watts", datetime.date(1990, 10, 29), new_school)
    school_class_1 = Homework18.SchoolClass("1-A", new_school, teacher_1)
    learner_1 = Homework18.Pupil("Tamara", "Hickman", datetime.date(2004, 2, 13), new_school)
    director_of_school.invite_new_pupil(school_class_1, learner_1)
    learner_2 = Homework18.Pupil("Rogelio", "Gibson", datetime.date(2004, 3, 16), new_school)
    director_of_school.invite_new_pupil(school_class_1, learner_2)
    teacher_1.add_marks(learner_1, 5)
    teacher_1.add_marks(learner_1, 7)
    teacher_1.add_marks(learner_2, 12)
    assert school_class_1.get_avg_mark() == 8.0


def test_school_avg_mark(new_school):
    director_of_school = Homework18.Director("Dean", "Winchester", datetime.date(1985, 8, 11), new_school)
    teacher_1 = Homework18.Teacher("Serena", "Watts", datetime.date(1990, 10, 29), new_school)
    school_class_1 = Homework18.SchoolClass("1-A", new_school, teacher_1)
    school_class_2 = Homework18.SchoolClass("1-B", new_school, teacher_1)
    learner_1 = Homework18.Pupil("Tamara", "Hickman", datetime.date(2004, 2, 13), new_school)
    director_of_school.invite_new_pupil(school_class_1, learner_1)
    learner_2 = Homework18.Pupil("Rogelio", "Gibson", datetime.date(2004, 3, 16), new_school)
    director_of_school.invite_new_pupil(school_class_2, learner_2)
    teacher_1.add_marks(learner_1, 10)
    teacher_1.add_marks(learner_1, 11)
    teacher_1.add_marks(learner_2, 3)
    assert new_school.get_avg_mark() == 8.0
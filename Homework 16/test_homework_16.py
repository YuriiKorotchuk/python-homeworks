import Homework16


# Task 1


def test_pupil_data():
    school_1 = Homework16.PrivateSchool("Hunt school")
    child_1 = Homework16.Pupil("Randall", "Zimmerman", 23, school_1)
    assert child_1.name == "Randall" and child_1.surname == "Zimmerman" and child_1.age == 23 and \
           child_1.school == school_1


def test_teacher_data():
    school_1 = Homework16.PrivateSchool("Hunt school")
    teacher_1 = Homework16.Teacher("Emmanuel", "Peters", 52, school_1)
    assert teacher_1.name == "Emmanuel" and teacher_1.surname == "Peters" and teacher_1.age == 52 and \
           teacher_1.school == school_1


def test_director_data():
    school_1 = Homework16.PrivateSchool("Hunt school")
    director_1 = Homework16.Director("Sophie", "Underwood", 49, school_1)
    assert director_1.name == "Sophie" and director_1.surname == "Underwood" and director_1.age == 49 and \
        director_1.school == school_1


def test_headteacher_data():
    school_1 = Homework16.PrivateSchool("Hunt school")
    headteacher_1 = Homework16.HeadTeacher("Terrance", "Brennan", 44, school_1)
    assert headteacher_1.name == "Terrance" and headteacher_1.surname == "Brennan" and headteacher_1.age == 44 and \
        headteacher_1.school == school_1


# Task 2


def test_pupils_quantity_1():
    school_1 = Homework16.PrivateSchool("Hunt school")
    teacher_1 = Homework16.Teacher("Emmanuel", "Peters", 52, school_1)
    cls1 = Homework16.SchoolClass("8-B", school_1, teacher_1)
    assert cls1.pupils_quantity() == 0


# Task 3


def test_added_pupil():
    school_1 = Homework16.PrivateSchool("Hunt school")
    teacher_1 = Homework16.Teacher("Emmanuel", "Peters", 52, school_1)
    cls1 = Homework16.SchoolClass("8-B", school_1, teacher_1)
    director_1 = Homework16.Director("Sophie", "Underwood", 49, school_1)
    pupil1 = Homework16.Pupil("Gilberto", "Rhodes", 15, school_1)
    director_1.invite_new_pupil(cls1, pupil1)
    assert cls1.pupils_quantity() == 1


def test_deleted_pupil():
    school_1 = Homework16.PrivateSchool("Hunt school")
    teacher_1 = Homework16.Teacher("Emmanuel", "Peters", 52, school_1)
    cls1 = Homework16.SchoolClass("8-B", school_1, teacher_1)
    director_1 = Homework16.Director("Sophie", "Underwood", 49, school_1)
    pupil1 = Homework16.Pupil("Gilberto", "Rhodes", 15, school_1)
    director_1.invite_new_pupil(cls1, pupil1)
    director_1.fire_pupil(cls1, pupil1)
    assert cls1.pupils_quantity() == 0

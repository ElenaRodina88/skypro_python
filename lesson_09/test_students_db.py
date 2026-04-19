from StudentTable import StudentTable

db = StudentTable('postgresql://postgres:7536@localhost:5432/QA')


def test_create_student():
    test_user_id = 999999

    students_before = db.get_students()

    db.create_student(test_user_id, 'beginner', 'group', 10)

    students_after = db.get_students()

    assert len(students_after) - len(students_before) == 1
    assert any(s[0] == test_user_id for s in students_after)

    db.delete_student(test_user_id)


def test_edit_student():
    test_user_id = 999999

    db.create_student(test_user_id, 'beginner', 'group', 10)
    db.update_student(test_user_id, 'advanced', 'personal', 10)

    student = db.get_students()

    updated_student = next(s for s in student if s['user_id'] == test_user_id)

    assert updated_student['level'] == 'advanced'
    assert updated_student['education_form'] == 'personal'

    db.delete_student(test_user_id)


def test_delete_student():
    test_user_id = 999999

    db.create_student(test_user_id, 'beginner', 'personal', 10)

    db.delete_student(test_user_id)

    students_after = db.get_students()

    assert not any(s[0] == test_user_id for s in students_after)

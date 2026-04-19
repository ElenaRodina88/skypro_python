from sqlalchemy import text, create_engine

class StudentTable:
    __scripts = {
        'select': text('SELECT * FROM student'),
        'insert_new': text('INSERT INTO student("user_id", "level", "education_form", "subject_id") '
                          'VALUES (:user_id, :level, :education_form, :subject_id)'),
        'update_student': text('UPDATE student SET "level" = :level, "education_form" = :education_form, '
                              '"subject_id" = :subject_id WHERE "user_id" = :user_id'),
        'delete by id': text("DELETE FROM student WHERE user_id = :user_id_to_delete")
    }

    def __init__(self, connection_string):
        self.__db = create_engine(connection_string)

    def get_students(self):
        return self.__db.execute(self.__scripts['select']).fetchall()

    def create_student(self, user_id, level, education_form, subject_id):
        self.__db.execute(self.__scripts['insert_new'], {'user_id': user_id, 'level': level,
                                                        'education_form': education_form, 'subject_id': subject_id})

    def update_student(self, user_id, level, education_form, subject_id):
        self.__db.execute(self.__scripts['update_student'], {'user_id': user_id, 'level': level,
                                                            'education_form': education_form, 'subject_id': subject_id})

    def delete_student(self, user_id):
        self.__db.execute(self.__scripts['delete by id'], user_id_to_delete=user_id)

from student import Student
from group import Course_group

student = Student('Alex', 'Popov', 19, 2)
student2 = Student('Masha', 'Ivanova', 19, 2)
student3 = Student('Petr', 'Petrov', 20, 2)

group = Course_group(student, [student2, student3])

classmates_str = ', '.join(f'{student.name} {student.surname}'
                           for student in group.classmates)

print(f'{group.student.name} {group.student.surname}, {group.student.age} лет,'
      f' учится на курсе {group.student.course} вместе с: {classmates_str}')

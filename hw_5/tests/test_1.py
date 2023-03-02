from hw_5.tasks.task_1 import Homework, Teacher, Student
student = Student("Ivan", "Vasilev")


def test_hw_in_time():
    homework = Teacher.create_homework("Learn functions", 0)
    assert student.do_homework(homework) is None


def test_hw_not_in_time():
    homework = Teacher.create_homework("create 2 simple classes", 5)
    assert student.do_homework(homework) == homework

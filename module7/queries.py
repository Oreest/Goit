from sqlalchemy import func, desc

from app.db import session
from app.db_models import Teacher, Student, Subject, Grade, Group


def select_1():
    """
    Знайти 5 студентів із найбільшим середнім балом з усіх предметів.
    :return: list[dict]
    """
    result = session.query(Student.fullname, func.round(func.avg(Grade.grade), 2).label('avg_grade')) \
        .select_from(Grade).join(Student).group_by(Student.id).order_by(desc('avg_grade')).limit(5).all()
    return result


def select_2(discipline_id: int):
    """
    Знайти студента із найвищим середнім балом з певного предмета.
    :return:
    """
    result = session.query(Subject.name, Student.fullname, func.round(func.avg(Grade.grade), 2).label('avg_grade')) \
        .select_from(Grade).join(Student).join(Subject).filter(Subject.id == discipline_id) \
        .group_by(Student.id, Subject.name).order_by(desc('avg_grade')).limit(1).all()
    return result


def select_3(discipline_id: int):
    """
    Знайти середній бал у групах з певного предмета.
    :return:
    """
    result = session.query(Subject.name, Group.name, func.round(func.avg(Grade.grade), 2).label('avg_grade')) \
        .select_from(Grade).join(Student).join(Subject).join(Group) \
        .filter(Subject.id == discipline_id).group_by(Group.id, Subject.id) \
        .order_by(desc('avg_grade')).all()
    return result


def select_4(group_id: int):
    """
    Знайти середній бал на потоці (по всій таблиці оцінок).
    :return:
    """
    result = session.query(Group.name, func.round(func.avg(Grade.grade), 2).label('avg_grade')) \
        .select_from(Grade).join(Student).join(Group).filter(Group.id == group_id) \
        .group_by(Group.name).all()
    return result


def select_5(teacher_id: int):
    """
    Знайти які курси читає певний викладач.
    :return:
    """
    result = session.query(Teacher.fullname, Subject.name) \
        .select_from(Teacher).join(Subject).filter(Teacher.id == teacher_id).all()
    return result


def select_6(group_id: int):
    """
    Знайти список студентів у певній групі.
    :return:
    """
    result = session.query(Student.fullname) \
        .select_from(Student).join(Group).filter(Group.id == group_id) \
        .group_by(Student.fullname).all()
    return result


def select_7(group_id: int, discipline_id: int):
    """
    Знайти оцінки студентів у окремій групі з певного предмета.
    :return:
    """
    result = session.query(Student.fullname, Subject.name, Grade.grade).select_from(Grade) \
        .join(Student).join(Subject).join(Group) \
        .filter(Group.id == group_id, Subject.id == discipline_id) \
        .order_by(Student.fullname).all()
    return result


def select_8(teacher_id: int):
    """
    Знайти середній бал, який ставить певний викладач зі своїх предметів.
    :return:
    """
    result = session.query(Teacher.fullname, Subject.name, func.round(func.avg(Grade.grade), 2).label('avg_grade')) \
        .select_from(Teacher).join(Subject).join(Grade) \
        .filter(Teacher.id == teacher_id) \
        .group_by(Teacher.fullname, Subject.name).all()
    return result


def select_9(student_id: int):
    """
    Знайти список курсів, які відвідує певний студент.
    :return:
    """
    result = session.query(Subject.name).select_from(Grade) \
        .join(Student).join(Subject) \
        .filter(Student.id == student_id) \
        .group_by(Subject.name).all()
    return result


def select_10(student_id: int, teacher_id: int):
    """
    Список курсів, які певному студенту читає певний викладач.
    :return:
    """
    result = session.query(Subject.name, Student.fullname, Teacher.fullname).select_from(Grade) \
        .join(Student).join(Subject).join(Teacher) \
        .filter(Student.id == student_id, Teacher.id == teacher_id) \
        .group_by(Subject.name, Student.fullname, Teacher.fullname).all()
    return result


if __name__ == '__main__':
    print(f'1.Знайти 5 студентів із найбільшим середнім балом з усіх предметів:\n{select_1()}\n')
    print(f'2.Знайти студента із найвищим середнім балом з певного предмета:\n{select_2(1)}\n')
    print(f'3.Знайти середній бал у групах з певного предмета:\n{select_3(1)}\n')
    print(f'4.Знайти середній бал на потоці (по всій таблиці оцінок):\n{select_4(1)}\n')
    print(f'5.Знайти які курси читає певний виклада:\n{select_5(1)}\n')
    print(f'6.Знайти список студентів у певній групі:\n{select_6(1)}\n')
    print(f'7.Знайти оцінки студентів у окремій групі з певного предмета:\n{select_7(1, 1)}\n')
    print(f'8.Знайти середній бал, який ставить певний викладач зі своїх предметів:\n{select_8(1)}\n')
    print(f'9.Знайти список курсів, які відвідує певний студент:\n{select_9(2)}\n')
    print(f'10.Список курсів, які певному студенту читає певний викладач:\n{select_10(1, 2)}')

# Задание 1
# Дан список учеников, нужно посчитать количество повторений каждого имени ученика
# Пример вывода:
# Вася: 1
# Маша: 2
# Петя: 2

students = [
    {'first_name': 'Вася'},
    {'first_name': 'Петя'},
    {'first_name': 'Маша'},
    {'first_name': 'Маша'},
    {'first_name': 'Петя'},
]
# ???

print('# Задание 1')
from collections import Counter
result = Counter([student['first_name'] for student in students])
for name in result:
    print(f"{name}: {result[name]}")


# Задание 2
# Дан список учеников, нужно вывести самое часто повторящееся имя
# Пример вывода:
# Самое частое имя среди учеников: Маша
students = [
    {'first_name': 'Вася'},
    {'first_name': 'Петя'},
    {'first_name': 'Маша'},
    {'first_name': 'Маша'},
    {'first_name': 'Оля'},
]
# ???
print('# Задание 2')
from collections import Counter
print('Самое частое имя среди учеников:', Counter([student['first_name'] for student in students]).most_common(1)[0][0])


# Задание 3
# Есть список учеников в нескольких классах, нужно вывести самое частое имя в каждом классе.
# Пример вывода:
# Самое частое имя в классе 1: Вася
# Самое частое имя в классе 2: Маша

school_students = [
    [  # это – первый класс
        {'first_name': 'Вася'},
        {'first_name': 'Вася'},
    ],
    [  # это – второй класс
        {'first_name': 'Маша'},
        {'first_name': 'Маша'},
        {'first_name': 'Оля'},
    ],[  # это – третий класс
        {'first_name': 'Женя'},
        {'first_name': 'Петя'},
        {'first_name': 'Женя'},
        {'first_name': 'Саша'},
    ],
]
# ???
print('# Задание 3')
from collections import Counter
for klass in school_students:
    print('Самое частое имя среди учеников:', Counter([student['first_name'] for student in klass]).most_common(1)[0][0])


# Задание 4
# Для каждого класса нужно вывести количество девочек и мальчиков в нём.
# Пример вывода:
# Класс 2a: девочки 2, мальчики 0 
# Класс 2б: девочки 0, мальчики 2

school = [
    {'class': '2a', 'students': [{'first_name': 'Маша'}, {'first_name': 'Оля'}]},
    {'class': '2б', 'students': [{'first_name': 'Олег'}, {'first_name': 'Миша'}]},
    {'class': '2б', 'students': [{'first_name': 'Даша'}, {'first_name': 'Олег'}, {'first_name': 'Маша'}]},
]
is_male = {
    'Олег': True,
    'Маша': False,
    'Оля': False,
    'Миша': True,
    'Даша': False,
}
# ???
print('# Задание 4')
[
    print(
        "Класс:", 
        klass['class'], 
        "девочки:", sum([int(not is_male[person]) for person in [student['first_name'] for student in klass['students']]]),
        "мальчики:", sum([int(is_male[person]) for person in [student['first_name'] for student in klass['students']]])
        ) 
        for klass in school
]

# Задание 5
# По информации о учениках разных классов нужно найти класс, в котором больше всего девочек и больше всего мальчиков
# Пример вывода:
# Больше всего мальчиков в классе 3c
# Больше всего девочек в классе 2a

school = [
    {'class': '2a', 'students': [{'first_name': 'Маша'}, {'first_name': 'Оля'}]},
    {'class': '3c', 'students': [{'first_name': 'Олег'}, {'first_name': 'Миша'}]},
]
is_male = {
    'Маша': False,
    'Оля': False,
    'Олег': True,
    'Миша': True,
}
# ???
print('# Задание 5')
school_stat = [   
        {
            klass['class']:
            {
                'girls': sum([int(not is_male[person]) for person in [student['first_name'] for student in klass['students']]]),
                'boys': sum([int(is_male[person]) for person in [student['first_name'] for student in klass['students']]]) 
            }
        } for klass in school
    ]

max_girls = {'klass': '', 'count': 0}
max_boys = {'klass': '', 'count': 0}
for klass_stat in school_stat:
    for klass, stat in klass_stat.items():
        if stat['girls'] > max_girls['count']:
            max_girls['klass'] = klass
            max_girls['count'] = stat['girls']
        if stat['boys'] > max_boys['count']:
            max_boys['klass'] = klass
            max_boys['count'] = stat['boys']
            
print(f"Больше всего мальчиков в классе {max_boys['klass']}")
print(f"Больше всего девочек в классе {max_girls['klass']}")

# Задание 1
# Необходимо вывести имена всех учеников из списка с новой строки

names = ['Оля', 'Петя', 'Вася', 'Маша']
# ???
print('# Задание 1')
[print(name) for name in names]

"""
for name in names:
    print(name)
"""

# Задание 2
# Необходимо вывести имена всех учеников из списка, рядом с именем показать количество букв в нём
# Пример вывода:
# Оля: 3
# Петя: 4

names = ['Оля', 'Петя', 'Вася', 'Маша']
# ???
print('# Задание 2')
[print(f"{name}: {len(name)}") for name in names]

"""
for name in names:
    print(f"{name}: {len(name)}")
"""

# Задание 3
# Необходимо вывести имена всех учеников из списка, рядом с именем вывести пол ученика

is_male = {
    'Оля': False,  # если False, то пол женский
    'Петя': True,  # если True, то пол мужской
    'Вася': True,
    'Маша': False,
}
names = ['Оля', 'Петя', 'Вася', 'Маша']
# ???
print('# Задание 3')
[print(name, 'мужской' if is_male[name] else 'женский') for name in names]

"""
for name in names:
    gender = 'мужской' if is_male[name] else 'женский'
    print(name, gender)
"""

# Задание 4
# Даны группу учеников. Нужно вывести количество групп и для каждой группы – количество учеников в ней
# Пример вывода:
# Всего 2 группы.
# Группа 1: 2 ученика.
# Группа 2: 4 ученика.

groups = [
    ['Вася', 'Маша'],
    ['Вася', 'Маша', 'Саша', 'Женя'],
    ['Оля', 'Петя', 'Гриша'],
]
# ???
print('# Задание 4')
print(f'Всего {len(groups)} группы.')
[print(f"Группа { groups.index(group) + 1 }: { len(group) } ученика.") for group in groups]

"""
print(f'Всего {len(groups)} группы.')
counter = 0
for group in groups:
    counter += 1
    print(f"Группа {counter}: {len(group)} ученика.")
"""

# Задание 5
# Для каждой пары учеников нужно с новой строки перечислить учеников, которые в неё входят
# Пример вывода:
# Группа 1: Вася, Маша
# Группа 2: Оля, Петя, Гриша

groups = [
    ['Вася', 'Маша'],
    ['Оля', 'Петя', 'Гриша'],
    ['Вася', 'Маша', 'Саша', 'Женя'],
]
# ???
print('# Задание 5')
[print(f"Группа { groups.index(group) + 1 }: { ', '.join([name for name in group]) } ") for group in groups]

"""
counter = 0
for group in groups:
    counter += 1
    print(f"Группа {counter}: ", end='')
    for pupil in group:
        print(pupil, end=', ')
    print()
"""
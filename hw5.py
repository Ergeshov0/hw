# задания1
# dictionary_1 = {'a': 300, 'b': 400}
# dictionary_2 = {'c': 500, 'd': 600}
# dictionary_1.update(dictionary_2)
# print(dictionary_1)

# задания2
# numbers = {'num_1' : 1, 'num_2' : 2, 'num_3' : 3, 'num_100' : 100}
# for key in numbers:
#     if isinstance(numbers[key], int):
#         numbers[key]*=5

# задания3
# student = {'name' : 'Askhat', 'age' : 17}
# student['age'] *=2
# print(student)
# задания4
# student = {'name' : 'Askhat', 'age' : 17, 'color' : 'White'}
# student['age'] = 16
# student['color'] = 'Black'
# print(student)

# задант5 
# student = {'name' : 'Askhat', 'age' : 17}
# student = dict(name='Askhat', age=17)
# del student['age']
# print(student)
# ###################################################
# задания6 
# student={'name' : 'Askhat'}
# student['address'] = 'Западный Анар'
# print(student)

# залания7

# student={
#     'Жони':20,
#     'Бека':20,
#     'Айка':20,
    
# }
# sorted = sorted(student.keys())
# for i in sorted:
#     print(i)
# 8
# student={
#     'Жони':90,
#     'Бека':95,
#     'Айка':99,
    
# }
# max =max(student,key=student.get)     
# print(max)

# 9
# num1={'a': 1, 'b': 2, 'c': 3}
# num2={'d':4, 'b': 5, 'n':6}

# result_num = {}

# for key, value in num1.items():
#     if key in result_num:
#         result_num[key] += value
#     else:
#         result_num[key] = value

# for key, value in num2.items():
#     if key in result_num:
#         result_num[key] += value
#     else:
#         result_num[key] =value

# print(result_num)

# 10
# students = [
#     {'name': 'жениш', 'отценка': [85, 90, 88]},
#     {'name': 'жонни', 'отценка': [92, 87, 89]},
#     {'name': 'жаныш', 'отценка': [78, 94, 91]},
# ]

# def calculate_average(grades):
#     return sum(grades) / len(grades)

# for student in students:
#     name = student['name']
#     grades = student['отценка']
#     average_grade = calculate_average(grades)
#     print(f"{name}: Средняя оценка - {average_grade}")

# #11 
# numbers = {
#     'A': 10,
#     'B': 15,
#     'C': 20,
#     'D': 5,
#     'E': 25,
# }

# sum_numbers = 0
# count = 0

# for value in numbers.values():
#     sum_numbers += value
#     count += 1

# average = sum_numbers / count

# closest_key = None
# min_difference = float('inf')

# for key, value in numbers.items():
#     difference = hash(value - average)
#     if difference < min_difference:
#         min_difference = difference
#         closest_key = key

# print(f"Ближайшим к среднему значению ({average}), это '{closest_key}' с числом {numbers[closest_key]}")

# 12
# products = [
#     {'name': 'сперма', 'price': 2.5},
#     {'name': 'нан', 'price': 1.0},
#     {'name': 'тукум', 'price': 1.2},
#     {'name': 'томатный сок', 'price': 3.0},
# ]

# total_cost = sum(product['price'] for product in products)

# print(f"Общая стоимость продуктов: {total_cost:.2f}")

# 13
# countries_capitals = {
#     'Россия': 'Москва',
#     'США': 'Вашингтон',
#     'Франция': 'Париж',
#     'Германия': 'Берлин',
# }

# while True:
#     country = input("Введите название страны (или 'выход' для завершения): ").strip()
    
#     if country.lower() == 'выход':
# #         break

# #     capital = countries_capitals.get(country, 'Столица не найдена')
# #     print(f"Столица страны {country}: {capital}")

# #14

# students = [
#     {'имя': 'жаныш', 'возраст': 20, 'оценки': [85, 90, 88]},
#     {'имя': 'жаныш', 'возраст': 19, 'оценки': [92, 87, 89]},
#     {'имя': 'жаныш', 'возраст': 21, 'оценки': [78, 94, 91]},
#     {'имя': 'жаныш', 'возраст': 17, 'оценки': [75, 82, 79]}
# ]

# max_grade = max(max(student['оценки']) for student in students)

# for student in students:
#     if max(student['оценки']) == max_grade and student['возраст'] > 18:
#         print(f"Студент {student['имя']} имеет максимальную оценку и возраст больше 18 лет.")

# passwords = set()

# password = input("Введите пароль: ")
# passwords.add(password)

# confirm_password = input("Подтвердите пароль: ")
# passwords.add(confirm_password)

# if len(password) < 8:
#     print("Короткий пароль!")
# elif '123' in password:
#     print("Простой пароль!")
# elif password != confirm_password:
#     print("Различаются.")
# else:
#     print("OK")
#     print("Пароль создан!")
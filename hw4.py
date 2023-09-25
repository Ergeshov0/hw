#задания1 

# it_company = ('Google' , 'Amazon' , 'Microsoft')
# num = list(it_company)
# num.append("Tesla")
# num1 =tuple(num)
# print(num1)

#Задача 2
# name =("1","2","3","4","5","6","7","8","9","10","Amazon","Googlo","Microsoft","Geeks","Osh","Bishkek","Nur","Russ","Bmw","Audi")
# print(name.index("Amazon"))

#задания3
# name =("1","2","3","4","5","6","7","8","9","10","Amazon","Googlo","Microsoft","Geeks","Osh","Bishkek","Nur","Russ","Bmw","Audi")
# num = list(name)
# num.pop(11)
# num.insert(11,"Apple")
# num1 =tuple(num)
# print(num1)

# name =("1","2","3","4","5","6","7","8","9","10","Amazon","Googlo","Microsoft","Geeks","Osh","Bishkek","Nur","Russ","Bmw","Audi")
# num =list(name)
# num[11]="Apple"
# num1 = tuple(num)
# print(num1)

#задания4
# name =("1","2","3","4","5","6","7","8","9","10","Amazon","Apple","Googlo","Microsoft","Geeks","Osh","Bishkek","Nur","Russ","Bmw","Audi")
# print(name[11:14])
#хадания 5
# text_tuple = ('Experienced', 'programmers', 'in', 'any', 'other', 'language', 'can', 'pick', 'up', 'Python', 
# 'very', 'quickly,', 'and', 'beginners', 'find', 'the', 'clean', 'syntax', 'and',
#  'indentation', 'structure', 'easy', 'to', 'learn.', 'Whet', 'your', 'appetite', 'with', 'our', 'Python', '3', 'overview')
# num = str(text_tuple)
# num1=num.lower()
# print(num1.count("python"))

# задания6
# name =("1","2","3","4","5","6","7","8","9","10","Amazon","Googlo","Microsoft","Geeks","Osh","Bishkek","Nur","Russ","Bmw","Audi")
# num = list(name)
# del num[3:9]
# num1 =["Алтын","Нур","Русс","Мак","маакбук"]
# num.extend(num1)
# name1 =tuple(num)
# print(name1)
# for element in name1:
#     print(element)

#задания 7
# num =[]
# for i in range(1,101):
#     num.append(i)
# print(num)

#задания 8
# num =list(range(1,1001))
# num1 =min(num)
# num2 =max(num)
# num3 =sum(num)
# print(num)
# print(num1)
# print(num2)
# print(num3)

# #задания 9
# for num in range(1,497):
#     if num % 2 == 0:
#          print(num)

#задания 10
# while True:
#         num1 = float(input("Введите первое число: "))
#         num2 = float(input("Введите второе число: "))
#         user = input("Выберите операцию (+, -, *, /) или 'Exit' для выхода: ")
#         if user == 'Exit':
#             break 
#         if user == '+':
#             print(num1 + num2)
#         elif user == '-':
#             print(num1 - num2)
#         elif user == '*':
#             print(num1 * num2)
#         elif user == '/':
#             print(num1 / num2)
#         else:
#             print("Error")

#Дп задания  1
# import random

# attempts = 5

# while attempts > 0:
#     print(f"У вас {attempts} попыток.")

#     user = input("Выберите (К)амень, (Н)ожницы или (Б)умага: ").lower()

#     if user not in ['к', 'н', 'б']:
#         print("Недопустимый выбор. Пожалуйста, выберите К, Н или Б.")
#         continue

#     choices = ['к', 'н', 'б']
#     computer = random.choice(choices)

#     if user == computer:
#         print("Ничья!")
#     elif (
#         (user == 'к' and computer == 'н') or
#         (user == 'н' and computer == 'б') or
#         (user == 'б' and computer == 'к')
#     ):
#         print("Вы выиграли!")
#     else:
#         print("Компьютер выиграл!")
#     attempts -= 1
    
# if attempts == 0:
#     print("Игра окончена, у вас осталось 0 попыток.")
    #задания 2
# while True:
#     a = int(input("Enter your age: "))
#     if a >= 18:
#         print("Доступ разрешен")
#         break
#     else:
#       print("Извините, пользование данным ресурсом только с 18 лет")
#задания 3
# num ="Hello, World!"
# print(num[::-1])
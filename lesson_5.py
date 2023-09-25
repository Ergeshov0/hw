# print(1.500+1.500)

# num=float(2)
# x=11
# y=12
# print(y+12+x)

# print(int(1.99999))

# # dict- словарь
# stubent={'name':'Geeks','age':2}
# print(stubent)
# print(stubent['age'])
# print(f"мне зовут {stubent['name']} мне {stubent['age']}года.")

# stubent['surname'] = 'Osh'
# print(stubent)
# keys = stubent.keys()
# print(keys)
# items = stubent.items()
# print(items)
# valuse = stubent.values()
# print(valuse)


# mum = int(input("ведите первое число"))
# num2 = int(input("ведите второе чимло"))
# print(f"результат после слодения: {num+num2}")
# print(f"результат после вычитая: {num-num2}")
# print(f"результат после умгожения: {num*num2}")
# print(f"результат после диления: {num/num2}")

# n =0
# while True:
#     n +=1
#     print(n)

# count = 0
# while count < 5:
#     print(count)
#     count += 1


# import random 

# user_health = 5
# bot_health =5 
# while True:
#     if user_health ==0 or bot_health ==0:
#         break
#     else:
#         bot = random.choice(["Камень", "Ножницы", "Бумага"])
#         user = input("Введите выбор:")
#         if user =="Камень":
#             if bot =="Камень":
#                 print(f"Ничья.У вас: {user_health}, у бота: {bot_health}")
#             elif bot =="Ножницы":
#                 bot_health-=1
#                 print(f"Вы выиграли.У вас: {user_health}, у бота: {bot_health}")
#             elif bot =="Бумага":
#                 user_health -=1
#                 print(f"Вы проиграли.У вас: {user_health}, у бота: {bot_health}")
#         elif user =="Ножницы":
#             if bot =="Камень":
#                 user_health -=1
#                 print(f"Вы проиграли.У вас: {user_health}, у бота: {bot_health}")
                
#             elif bot =="Ножницы":
#                 print(f"Ничья.У вас: {user_health}, у бота: {bot_health}")
#             elif bot =="Бумага":
#                 bot_health-=1
#                 print(f"Вы выиграли.У вас: {user_health}, у бота: {bot_health}")
                
                
#         elif user =="Бумага":
#             if bot =="Камень":
#                 bot_health-=1
#                 print(f"Вы выиграли.У вас: {user_health}, у бота: {bot_health}")
#             elif bot =="Ножницы":
#                 user_health -=1
#                 print(f"Вы проиграли.У вас: {user_health}, у бота: {bot_health}")
#             elif bot =="Бумага":
#                 print("Ничья")
#         else:
#             print("Неверный вариант")

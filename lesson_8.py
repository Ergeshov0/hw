# summ = lambda num1, num2: num1+num2
# nu1 = int(input("ведите чисдо: "))
# nu2 = int(input("ведите чисдо: "))
# result = summ(nu1,nu2)
# print(f"результат: {result}")

# listter = [1,2,3,4,5,6,7,8,9,10]
# result = list(map(lambda i : i*2,listter))
# print(result)

# names = ["Mergul", "Erbol", "Rasul", "Nurai"]
# result = list(map(lambda i: f"{i} - {len(i)} букв",names))
# print(f"резултат:{result}")

# file_write = open('users,txt', 'w')
# file_write.write("привет,меня зовут Geeks и мне  2 года")
# file_write.close()

# file_read = open('users,txt', 'r')
# result = file_read.read()
# print(f"результат: {result}")

# names = ["Mergul", "Erbol", "Rasul", "Nurai"]
#1 способ
# file_write = open('names.txt', 'w')
# for i in names:
#     file_write.write(f"имя: {i}. \n")

# file_write.close()

# file_read = open('names.txt', 'r')
# resul = file_read.read()
# print(resul)

# 2 способ
# with open("names", 'w') as file_write:
#     for i in names:
#         file_write.write(f"имя: {i}. \n")

# with open("names.txt", 'r') as file_read:
#     result = file_read.read()
#     print(result)

# with open('python.py', 'w') as write:
#     write.writewith open("names", 'w') as file_write:
#     for i in names:
#         file_write.write(f"имя: {i}. \n")

# with open("names.txt", 'r') as file_read:
#     result = file_read.read()
#     print(result)
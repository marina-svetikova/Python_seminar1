#Вывести квадрат числа

# a = int(input())
# print(a**2)

#Напишите программу, которая на вход принимает два числа и прверяет 
# является ли одно число квадратом дургого

# a = int(input('A:'))
# c = int(input('C:'))

# if c//a == a: #так лучше не делать потому что 0 на 0 делить нельзя будет ошибка
#     print('Является')
# else:
#     print('Не является  ')

# if a**2 == c: #второй варинат без деления
#     print('Является')
# elif c**2 == a: 
#     print('Является')
# else:
#     print('Не является')

# if a**2 == c or c**2 == a:
#     print('Является')
# else:
#     print('Не является')

#Напишите прграмму, которая на вход принимает 
# 5 и находит мах из них

a=input().split() #список из элементов, состоит из строковых элементов
print(a)
max = int(a[0])
for i in range(5):
    if int(a[i])>max:
        max = int(a[i])
print(max)
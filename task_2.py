#Напишите прграмму, которая на вход принимает 
# 5 и находит мах из них

# a=input().split() #список из элементов, состоит из строковых элементов
# print(a)
# max = int(a[0])
# for i in range(5):
#     if int(a[i])>max:
#         max = int(a[i])
# print(max)

# a = input().split() #список из элементов, состоит из строковых элементов
# print(a)
# max = int(a[0])
# for i in range(len(a)): # если хоти что бы список шел в обратном порядке с конца то шаг раве-2 (напрмиер) range(6,0,-1)
#     if int(a[i])>max:
#         max = int(a[i])
# print(max)

a = list(map(int, input().split())) #решение в 1 строку с помощью функции мах
print(max(a))
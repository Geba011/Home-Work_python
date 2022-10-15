#15
#n = int(input("Введите число: "))
#list1=[]
#f = 1
#list1.append(f)
#for i in range(2, n+1):
#     f *= i
#      list1.append(f)
#print(list1)      


  #Сумма цифр вещественного числа. 


#numbers = float(input('Введите число: '))
#summa = 0 
#while numbers !=0:
#    a  = numbers%10
#    summa = summa + a
#    numbers = numbers //10
#print(summa)    

#Задача 14

from curses.ascii import isdigit
import symbol

nums = input('Введите число ')
summ = 0

for symbol in nums:
    if symbol.isdigit():
          summ = summ +int(symbol)
    
print(summ)   


#Задача 16
n = int(input())
list_n = []
for i in range(1,n+1):
    p = (1+ 1/i)**i
    list_n.append(round(p,3))
print((list_n))
total = 0

print(sum(list_n))


# Алгоритм смешивания элементов списка 

import random

list =input('Введите элементы списка через пробел:').split()
print(list)
for _ in range(random.randint(1,10)):  # количество смен 
    index1 = random.randint(0 , len(list) - 1 )
    index2 = random.randint(0 , len(list) - 1 )
list[index1],list[index2] =  list[index2],list[index1]

print(list)



     
     
     
     



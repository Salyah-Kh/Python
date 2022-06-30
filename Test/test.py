import math

#task1
age=26
print("Мне " +str(age)+ " лет")

#task2
#print ("Давайте познакомимся!")
#name = input ("Введите свое имя: ")
#age = input ("Укажите свой возраст: ")
#print ("привет " +name)
#print("Твой возраст: "+age)

#task3
# + - * / унарный минис
d=3
b=55
c=d+b
print (c)

#task4
a=2.65666
#округление в большую сторону
print( round(a) )
#округление в меньшую сторону
print( math.floor(a) )
#округление в, большую сторону
print( math.ceil(a) )
#число пи
print( math.pi )

#простой калькулятор v1

what =input ("Что делаем ? (+, -): ")

t = float (input ("Введи 1 число: "))
m = float (input ("Введи 2 число: "))

if what == "+":
    p=t+m 
    print ("Результат: " + str (p))
elif what == "-":
    p=t-m 
    print ("Результат: " + str (p))
else:
    print ("Неверная операция")
    
























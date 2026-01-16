print("hello") #for one word print
print("My name is xyz ","My age is A") #for multipel sentence print
print(25) #for number print

#variable 
name = "xyz"
age = 23
price = 25.99
old = False
a = None

print(name)
print(age)
print(25.99)
print(name,age,price)

#to know variable type
print(type(name))
print(type(age))
print(type(25.99))
print(type(old))
print(type(a))

#Arithmetic Opration
x = 5
y = 10 

print(x + y)
print(x - y)
print(x*y)
print(x/y)
print(x%y) #reminder
print(x**y) #x^y

#Relational opration
x = 5
y = 10

print(x == y)
print( x != y)
print(x>y)
print(x>=y)
print(x<y)
print(x<=y)

#Assignment opration

x= 5
x += 5
# x -= 5
# x *= 5
# x %= 5
# x **= 5
print(x)

#logical opration
x = 5
y = 10
print(not x > y)
print(not x < y)
print(x and y)
print(x or y)

#type conversion

x1=int("5")
y1=10.23
sum = x1 + y1
print(sum)

#input in python #to get value from user
name = input("enter your name:")
print("your name is:",name)

val =input("enter some values")
print("value type is",type(val))
#1. Write a program to add two numbers
a = int(input("Enter First Number: "))
b = int(input("Enter Second Number: "))
print(a+b)

#2. Write a program print Hello World
print("Hello World")

#3. Write a program Find & Calculate Square Root
#type - 1
num = int(input("Enter a number for square root: "))
root = num**0.5
print(root)
#type - 2
import math
num1 = int(input("Enter a number for square root: "))
root1 = math.sqrt(num1)
print(root1)
#type - 3
import cmath
num2 = int(input("Enter a number for square root: "))
root2 = cmath.sqrt(num2)
print(root2)

#4. Write a program to calculate area of Triangle
#type - 1
base = int(input("Enter base value for area of triangle: "))
height = int(input("Enter height value for area of triangle: "))
area = 0.5*base*height
print(area)
#type - 2
side1 = int(input("Enter first side value of triangle: "))
side2 = int(input("Enter second side value of triangle: "))
side3 = int(input("Enter third side value of triangle: "))
s = (side1+side2+side3)/2
area1 = (s*(s-side1)*(s-side2)*(s-side3))**0.5
print(area1)
#type - 3
import math
side4 = int(input("Enter first side value of triangle: "))
side5 = int(input("Enter second side value of triangle: "))
angle = float(input("Enter angle value between two side: "))
area2 = 0.5*side4*side5*(math.sin(math.radians(angle)))
print(area2)

#5. Write a program swap to variable
#type - 1
var1 = int(input("Enter first variable: "))
var2 = int(input("Enter second variable: "))
var2, var1 = var1, var2
print("first variable is",var1,"second variable is",var2)
#type - 2
var3 = int(input("Enter first variable: "))
var4 = int(input("Enter second variable: "))
temp = var3
var3 = var4
var4 = temp
print("first variable is",var3,"second variable is",var4)

#6. Write a program to check number positive, negative or zero
#type - 1
num = int(input("Enter a number for check positive, negative or zero: "))
if num>0:
    print(num,"number is positive")
elif num<0:
    print(num,"number is negative")
else:
    print(num,"number is zero")
#type - 2
num1 = int(input("Enter a number for check positive, negative or zero: "))
match num1:
    case num1 if num1>0:
        print(num1,"number is positive")
    case num1 if num1<0:
        print(num1,"number is negative")
    case _ :
        print(num1,"number is zero")

#7. Write a program to convert kilometer to miles
kilo = int(input("Enter a kilometer number for convert miles: "))
mile = kilo*0.6214
print(mile)

#8. Write a program to check number odd or even
num = int(input("Enter a number for check odd or even: "))
if num%2==0:
    print(num,"number is even")
else:
    print(num,"number is odd")

#9. Write a program to find the largest among three number
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
num3 = int(input("Enter third number: "))
if num1>num2 and num1>num3:
    print(num1,"is largest")
elif num2>num3 and num2>num1:
    print(num2,"is largest")
else:
    print(num3,"is largest")
#type - 2
num4 = int(input("Enter first number: "))
num5 = int(input("Enter second number: "))
num6 = int(input("Enter third number: "))
largest_number = max(num4,num5,num6)
print(largest_number)

#10. Write a program to check prime number
num = int(input("Enter a number for check prime number or not: "))
for i in range(2,num):
    if num%i==0:
        print(num,"is not prime number")
        break
else:
    print(num,"is prime number")
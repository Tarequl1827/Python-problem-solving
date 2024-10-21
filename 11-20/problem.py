#11. Write a program to generate a random number
#type - 1
import random
random_number = random.randint(10,20)
print(random_number)
#type - 2
import random
random_number1 = random.randrange(20)
print(random_number1)

#12. Write a program to convert celsius to fahrenheit
celsius = float(input("Enter celsius value: "))
fahrenheit = ((9*celsius)/5)+32
print(fahrenheit)

#13. Write a program to find the factorial of a number
#type - 1
num = int(input("Enter a number for find factorial: "))
import math
fact = math.factorial(num)
print(fact)
#type - 2
num1 = int(input("Enter a number for find factorial: "))
fact1 = 1
for i in range(num1,0,-1):
    fact1 *= i
print(fact1)
#type - 3
num2 = int(input("Enter a number for find factorial: "))
fact2 = 1
for i in range(1,num2+1):
    fact2 *= i
print(fact2)
#type - 4
num3 = int(input("Enter a number for find factorial: "))
def fact(n):
    if n==1:
        return 1
    else:
        return n*fact(n-1)
print(fact(num3))

#14. Write a program to display the multiplication table
#type - 1
num = int(input("Enter a number for display multiplication table: "))
for i in range(1,11):
    print(num,"x",i,"=",num*i)
#type - 2
num1 = int(input("Enter a number for display multiplication table: "))
j = 1
while j<=num1:
    print(num1,"x",i,"=",num*i)

#15. Write a program to fibonacci sequence
#type - 1
first_number = 0
second_number = 1
print(first_number, end=" ")
print(second_number, end=" ")
for i in range(10):
    sum = first_number + second_number
    first_number = second_number
    second_number = sum
    print(sum, end=" ")
    i+=1
#type - 2
print() #use for line break
first_number1 = 0
second_number1 = 1
print(first_number1, end=" ")
print(second_number1, end=" ")
def fibo(f,s):
    for i in range(10):
        sum = f + s
        f = s
        s = sum
        print(sum, end=" ")
        i += 1
fibo(first_number1, second_number1)
#type - 3
print()
first_number2 = 0
second_number2 = 1
print(first_number2, end=" ")
print(second_number2, end=" ")
def fibo1(f,s):
    if f>50:
        return 1
    else:
        sum = f + s
        print(sum, end=" ")
        fibo1(s, sum)
fibo1(first_number2, second_number2)

#16. Write a program to print all prime number in an interval
#type - 1
for i in range(2,30):
    for j in range(2,i):
        if i%j==0:
            print(i,"not a prime number")
            break
    else:
        print(i,"prime number")
#type - 2
for i in range(2,30):
    for j in range(2,i):
        if i%j==0:
            break
    else:
        print(i,"prime number")
#17. Write a program to find the sum of natural numbers.
num = int(input("Enter a natural number: "))
sum = 0
for i in range(1,num):
    sum+=i
print(sum)

#18. Write a program to check leap year
year = int(input("Enter a year to know about leap year: "))
if year%400==0 and year%100==0:
    print(year,"leap year")
elif year%4==0 and year%100!=0:
    print(year,"leap year")
else:
    print(year,"not leap year")

#19. Write a program to check if the number is armstrong or not
num = int(input("Enter a number to know armstrong or not: "))
temp = num
first_value = temp//100
temp%=100
second_value = temp//10
temp%=10
third_value = temp
sum = first_value**3 + second_value**3 + third_value**3
if sum==num:
    print(num,"is armstrong")
else:
    print(num,"is not armstrong")

#20. Write a program to find armstrong number in an interval
lower = int(input("Enter lower number of armstrong: "))
upper = int(input("Enter upper number of armstrong: "))
for i in range(lower,upper+1):
    temp = i
    first_value = temp // 100
    temp %= 100
    second_value = temp // 10
    temp %= 10
    third_value = temp
    sum = first_value ** 3 + second_value ** 3 + third_value ** 3
    if sum == i:
        print(i, "is armstrong")
    else:
        print(i, "is not armstrong")
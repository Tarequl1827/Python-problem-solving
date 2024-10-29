#21. Write a program to find factorial of number using recursion
num = int(input("Enter a number: "))
def fact(n):
    if n==1:
        return 1
    else:
        return n*fact(n-1)
print(fact(num))

#22. Write a program to sum of natural numbers using recursion
first = 0
second = 1
def sum(f,s):
    if f>10:
        return 1
    else:
        add = f + s
        print(add)
        s+=1
        sum(add,s)
sum(first,second)

#23. Write a program to display fibonacci sequence using recursion
first = 0
second = 1
print(first)
def fibo(f,s):
    if f>50:
        return 1
    else:
        add = f + s
        print(add)
        s  = f
        fibo(add,s)
fibo(first,second)

#24. Write a program to make a simple calculator
fistNumber = float(input("Enter first number: "))
operator = input("What are you want to do ( +, -, *, / ): ")
secondNumber = float(input("Enter second number: "))
match operator:
        case '+':
            sum = fistNumber + secondNumber
            print(sum)
        case '-':
            sum = fistNumber - secondNumber
            print(sum)
        case '*':
            sum = fistNumber * secondNumber
            print(sum)
        case '/':
            sum = fistNumber / secondNumber
            print(sum)
        case '=':
            print(sum)
while True:
    ope = input("What are you want to do (+, -, *, /, = ): ")
    if ope!='=':
        fistNumber = sum
        secondNumber = float(input("Enter second number: "))
    else:
        print("Final result is: ",sum)
        break
    match ope:
        case '+':
            sum = fistNumber + secondNumber
            print(sum)
        case '-':
            sum = fistNumber - secondNumber
            print(sum)
        case '*':
            sum = fistNumber * secondNumber
            print(sum)
        case '/':
            sum = fistNumber / secondNumber
            print(sum)

#25. Write a program to find the factorial of a number
#type - 1
num = int(input("Enter a number for find factorial: "))
fact = 1
for i in range(1,num+1):
    fact *=i
print(fact)
#type - 2
num1 = int(input("Enter a number for find factorial: "))
def fact(n):
    if n==1:
        return 1
    return n*fact(n-1)
print(fact(num1))

#26. Write a program to display powers of 2 using anonymous function.
#type - 1
num = int(input("Enter a number: "))
power = (lambda x:x**2)
print(power(num))
#type - 2
num1 = int(input("Enter a number: "))
result = list(map(lambda x:2**x,range(num1-1)))
print(result)
for i in range(num1-1):
    print("The result of 2 raised to power",i,"is",result[i])

#27. Write a program to find numbers divisible by another number
#type - 1
num = list(range(1,100))
division = int(input("Enter a number: "))
for i in num:
    if i%division==0:
        print(i)
#type - 2
for i in range(1,100):
    if i%division==0:
        print(i)
#type - 3
l = list(range(1,30))
result = list(filter(lambda x: x%13==0, l))
print(result)
#type - 4
result = list(filter(lambda x: x%13==0, range(1,30)))
print(result)

#28. Write a program to convert decimal to binary,octal and hexadecimal
num = int(input("Enter a decimal number here: "))
print(bin(num),"in binary")
print(oct(num),"in octal")
print(hex(num),"in hexadecimal")
#type - 2
num1 = int(input("Enter a decimal number here: "))
l = []
while num1>0:
    num = num1 // 2
    result = num1 % 2
    num1 = num
    l.insert(0,result)
for i in l:
    print(i,end="")

#29. Write a program to find ascii value
var = input("Enter a character: ")
print("The ASCII value of",var,"is",ord(var))

#30. Write a program to find hcf or gcd
a = 12
b = 30
for i in range(2,(a*b)+1):
    if a%i==0 and b%i==0:
        print(i)
        break
for i in range(2,(a*b)+1):
    if i%a==0 and i%b==0:
        print(i)
        break
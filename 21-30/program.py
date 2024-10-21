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


#31. Write a program to find factor
num = int(input("Enter a number: "))
for i in range(1,num+1):
    if num%i==0:
        print(i)

#32. Write a program to shuffle deck of cards
import random,itertools
deck = list(itertools.product(range(1,14),["Spade","Clud""Hearts","Diamond"]))
random.shuffle(deck)
for i in range(5):
    print(deck[i][0],"of",deck[i][1])
    break

#33. Write a program to display calendar
import calendar
year = int(input("Enter year: "))
month = int(input("Enter month number: "))
calendar = calendar.month(year,month)
print(calendar)

#34. Write a program to convert decimal to binary using recursion
number = int(input("Enter a decimal number: "))
l = []
def con(n):
    if n>0:
        con(n//2)
        print(n%2,end="")
con(number)
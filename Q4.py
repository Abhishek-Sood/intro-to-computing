#Q1
marks= (int(input("Enter your marks : ")))
if marks<25:
    print("F")
elif marks>=25 and  marks <45 :
    print("E")
elif marks>=45 and marks < 50:
    print("D")
elif marks>=50 and marks < 60:
    print("C")
elif marks>=60 and marks < 80:
    print("B")
else:
    print("A")

#Q2
year = int(input("Enter year to be checked : "))
if (year % 400 == 0) and (year % 100 == 0):
    print(year,"is a leap year")

elif (year % 4 ==0) and (year % 100 != 0):
    print(year,"is a leap year")

else:(print("not a leap year"))

import random
import math

for i in range (1,11):
    num1 = random.randint(1,10)
    num2 = random.randint(1,10)
    print ("Question",i,":",num1,"*",num2,"=", end = " ")
    guess = int (input())
    answer = num1*num2
    if guess == answer:
        print ("Right!")
    else:
        print ("Wrong. The answer is: ",answer)

for candies in range(200):
    if (candies % 5 != 2):
        continue
    if (candies % 6 != 3):
        continue
    if (candies % 7 != 2):
        continue

    print(str(candies) + " is the answer!")
    break
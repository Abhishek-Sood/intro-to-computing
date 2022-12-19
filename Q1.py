#Q1
a = int(input("enter first number : "))
b = int(input("enter second number : "))
c = int(input("enter third number : "))

average = (a + b + c) / 3

print ("Average is : ", average )

#Q2
GrossIncome = int(input("enter your income : "))
NoOfDependents = int(input("enter no of dependents : "))
StandardDeduction = 10000
DependentDeduction = 3000
TaxRate = 0.2
TaxableIncome = (GrossIncome - StandardDeduction - (DependentDeduction * NoOfDependents))
Tax = TaxableIncome * TaxRate
print ("your tax is : ",Tax)

#Q3
NumberOfSeconds = int(input("Enter number of seconds"))
Minutes = NumberOfSeconds // 60
Seconds = NumberOfSeconds % 60
print (Minutes, "Minutes and", Seconds, "Seconds")

#Q4
a = 25
b = '25'
c = 25.0

result = a + int(b) + c

print (str(result))

#Q5
import math

print("Sin values : ")
for Degree in range (0,346,15):
    i = math.sin(math.radians(Degree))
    a = round(i, 4)
    print(a)

print("Cosine values : ")
for Degree2 in range (0,346,15):
    j = math.cos(math.radians(Degree2))
    b = round(j,4)
    print(b) 
#1
a = "Python is a case sensitive language"
print(len(a))
print("".join(reversed(a)))
x = slice(10, 26, +1)
print(a[x])
y = a.replace("a case sensitive", "object oriented")
print(y)
z = a.index("a")
print(z)
a = a.strip()
print(a)

#2
Name = "Abhishek Sood"
SID = 22104019
DepartmentName = "Electrical Engineering"
CGPA = 9.9

print(" Hey", Name, "here!", "\n", "My SID is", SID, "\n", "I am from", DepartmentName, "department and my CGPA is", )

#3
a = 56
b = 10
print(a & b)
print(a | b)
print(a ^ b)
print(a << 2)
print(b << 2)
print(a >> 2)
print(b >> 4)

#4
a = int(input("Number1 : "))
b = int(input("Number2 : "))
c = int(input("Number3 : "))

print("Maximum of the above three numbers is : ", max(a, b, c))

#5
Name = input()
if 'name' in Name:
    print('yes')
else:
    print('no')

#6
a = input("Enter first side length : ")
b = input("Enter second side length : ")
c = input("Enter third side length : ")

if (a + b < c) and (b + c < a) and (a + c < b) :
    print("No")
else:
    print("Yes")
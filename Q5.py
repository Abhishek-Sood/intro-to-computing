#1
string = input("Enter the string to reverse: ")
print(string[::-1])

#2
start = int(input("Enter the start of the range: "))
end = int(input("Enter the end of the range: "))
divisor = int(input("Enter the number to check divisibility by: "))
for num in range(start, end+1):
  if num % divisor == 0:
    print(num)

#3
import math
a = float(input("Enter side a: "))
b = float(input("Enter side b: "))
c = float(input("Enter side c: "))
if a + b > c and a + c > b and b + c > a:
  s = (a + b + c) / 2
  area = math.sqrt(s * (s - a) * (s - b) * (s - c))
  print("The area of the triangle is", area)
else:
  print("The combination of sides is not possible.")

#4
  for row in range(9):
    for column in range(5):
        if row <= 4:
            if column <= row:
                print("*", end=" ")
        else:
            if column >= row-4:
                print("*", end=" ")
        print()

#5
char = 65
n = int(input("Enter the number of rows: "))
for i in range(1, n+1):
  for j in range(i):
    print(chr(char), end="")
    char += 1
    if char > 90:
      char = 65
  print()

#6
start = int(input("Enter the start of the range: "))
end = int(input("Enter the end of the range: "))
for num in range(start, end+1):
  is_prime = True
  for i in range(2, num):
    if num % i == 0:
      is_prime = False
      break
  if is_prime:
    print(num)

#7
start = 1
end = 500
for num in range(start, end+1):
  if num % 7 == 0 and num % 11 == 0:
    print(num)

#8
positives = []
negatives = []
odds = []
evens = []
count = {}
for i in range(10):
  num = int(input("Enter an integer: "))
  if num > 0:
    positives.append(num)
  elif num < 0:
    negatives.append(num)
  if num % 2 == 0:
    evens.append(num)
  else:
    odds.append(num)
  if num in count:
    count[num] += 1
  else:
    count[num] = 1
print("Positive numbers:", *positives)
print("Negative numbers:", *negatives)
print("Odd numbers:", *odds)
print("Even numbers:", *evens)
print("Number count:", count)

#9
words = input("Enter a list of words separated by space: ").split()
count = {}
for word in words:
  if word in count:
    count[word] += 1
  else:
    count[word] = 1
print("Word count:", count)
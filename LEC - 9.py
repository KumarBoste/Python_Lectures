'''
----------------------------------------------
----------------------------------------------
# DAY - 9 :
----------------------------------------------
----------------------------------------------
'''
 
# Iterator and Iterable

for i in range(1,10):
  print(i)  # i is called iterator


# Calculate length of each string  

## Define a iterable :  List
lst = ["Hello","World","PythonProgramming","DataScinece","Java"]

bucket1 = []
bucket2 = []

for i in lst:
  if len(i) > 5:
    bucket1.append(i)
  else:
    bucket2.append(i)
print(bucket1)
print(bucket2)


# Lambda Function

x = lambda x: x**2
print(x(5))
# Calculate length of each string using def function

## Define a iterable :  List
lst = ["Hello","World","PythonProgramming","DataScinece","Java"]

def compute():  #Function definition

  bucket1 = []
  bucket2 = []

  for i in lst:
    if len(i) > 5:
      bucket1.append(i)
    else:
      bucket2.append(i)
  return bucket1,bucket2

bucket1,bucket2 = compute()  # Function Calling
print(bucket1)
print(bucket2)

# Vowels Program

lst1 = ["a","e","h","k","o","u"]

bucket1 = []
bucket2 = []

for i in lst1:
  if i in "aeiou":
    bucket1.append(i)
  else:
    bucket2.append(i)

print(bucket1)
print(bucket2)


# Vowels Program using def

lst1 = ["a","e","h","k","o","u"]
def compute2():
  bucket1 = []
  bucket2 = []

  for i in lst1:
    if i in "aeiou":
      bucket1.append(i)
    else:
      bucket2.append(i)
  return bucket1,bucket2

bucket1,bucket2 = compute2()
print(bucket1)
print(bucket2)


# Lambda Function

x = lambda x: x**2
print(x(5))

# Add Function using Add
## computing  addition using lambda function

add =  lambda a,b: a+b
print(add(100,200))

## computing  addition using def function

def sum(a,b): # function definition
 a = 100
 b = 200
 return a+b

sum(100,200) # function calling


# print whether the number is even or odd using def function
import time
start = time.perf_counter()
number = int(input("Enter the Number: "))

def number1():
  if number % 2 == 0:
    print("Even Number")
  else:
    print("Odd Number")
number1()
end = time.perf_counter() - start
print('{:.6f}s for the calculation'.format(end))


# print whether the number is even or odd using lambda function
import time
start = time.perf_counter()

x = lambda number: "Even Number" if number % 2 == 0 else "Odd Number"
print(x(5))

end = time.perf_counter() - start
print('{:.6f}s for the calculation'.format(end))

marks = lambda x: "Best" if x >= 90 else ("Median" if x >= 75 else "Poor")
print(marks(73)) 



# Calculator Program Using DEF FUNCTION

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        return "Error: Cannot divide by zero!"
    return a / b

print("Simple Calculator using  Def-Functions")
print("1. Add\n2. Subtract\n3. Multiply\n4. Divide")

choice = int(input("Enter choice (1-4): "))
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

if choice == 1:
    print("Result:", add(num1, num2))
elif choice == 2:
    print("Result:", subtract(num1, num2))
elif choice == 3:
    print("Result:", multiply(num1, num2))
elif choice == 4:
    print("Result:", divide(num1, num2))
else:
    print("Invalid choice!")

# Calculator Program using LAMBDA FUNCTION

add = lambda a, b: a + b
subtract = lambda a, b: a - b
multiply = lambda a, b: a * b
divide = lambda a, b: "Error: Cannot divide by zero!" if b == 0 else a / b

print("Simple Calculator using Lambda Functions")
print("1. Add\n2. Subtract\n3. Multiply\n4. Divide")

choice = int(input("Enter choice (1-4): "))
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

operations = {
    1: add,
    2: subtract,
    3: multiply,
    4: divide
}

if choice in operations:
    print("Result:", operations[choice](num1, num2))
else:
    print("Invalid choice!")


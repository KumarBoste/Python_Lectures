'''
----------------------------------------------
----------------------------------------------
# DAY - 16 :
----------------------------------------------
----------------------------------------------
'''

# Build in Function 

# |-1| = 1 , |2|= 2

num = abs(-1)
print(num)

num1 = abs(2)
print(num1)

num2 = 3.40111411111111
print(round(num2))

import math

num3 = 3.112234444444
print(math.ceil(num3))
print(math.floor(num3))
print(math.pi)
print(math.pow(2,3))
print(2**3)

# Write a program : Factorial

# !4 = 4*3*2*1 = 24

num = int(input("Enter the Number: "))

fact = 1

def factorial(num):
  if num == 0 or num == 1:
    return 1

  else:
    for i in range(1,num+1):
      # !4 = 4*3*2*1 = 24
      return num * factorial(num-1)
factorial(num)

# Using Math 

print(math.factorial(num))


# sin(30) = 0.5

print(math.sin(math.radians(30)))
print(math.cos(math.radians(30)))
print(math.tan(math.radians(30)))
print(math.cosh(math.radians(30)))

print(math.sqrt(25))

'''
----------------------------------------------
----------------------------------------------
# DAY - 8 :
----------------------------------------------
-----
'''
# Defining a Function
'''
def () = # Function Definition
    statements
    Expressions
    return statements,expression
a,b = () # Function Calling
'''

# ---------------------------------------------------------------
def sum():  # Function Definition
  num1 = 100
  num2 = 200

  num3 = num1 + num2
  return num3

ans = sum ()  # Function Calling 
print (f"The addition of two number is {ans}")  # Using F- String Function

def sum():   # Function Definition
  num1 = float(input("Enter the First Number : "))
  num2 = float(input("Enter the Second Number : "))

  num3 = num1 + num2
  return num3

ans = sum ()  # Function Calling 
print (f"The addition of two number is {ans}")  # Using F- String Function




# -------------------------------------------------------------------------
def sum() :     # Function Definition
  a =  float(input("Enter the First Number : "))
  b = float(input("Enter the Second Number : "))

  return(a+b)

  ans = sum(1,1) # Function Calling
  print(f"The addition of two number is {ans}")  # Using F- String Function)


# -------------------------------------------------------------------------
def student_info(name,Age,Gender):  # Function Definition
  print(f"The name of Student is {name}")
  print(f"The Age of Student is {Age}")
  print(f"The Gender of Student is {Gender}")

student_info(name = "varun",Age = 20, Gender = "Male") # function calling with parameters


# ------------------------------------------------------------------------------------------

number1 = float(input("Enter the First number : "))
number2 = float(input("Enter the Second number : "))

def sum():   #function definition
  number3 = number1 + number2
  return number3

def sub(): #function definition
    number3 = number1 - number2
    return number3
  
ans1 = sum() # Function calling
ans2 =sub() # Function calling
print(ans2)
print(ans1)


#------------------------------------------------------------------------------------------------------

# write a function whether the given string is palindrom or not

string = input("Enter the String: ")

def palindrom():  # function definition
  string1 = string[::-1]

  if string == string1 :
    print("The Given String is Palindrom")
  else:
    print("The Given String is not Palindrom")

palindrom() # function calling

# ----------------------------------------------------------------------------------------------------------
even = []
odd  = []

for i in range(1,30):
  if i % 2 == 0:
    even.append(i)
  else:
    odd.append(i)
print(even)
print(odd)


# ---------------------------------------------------------------------------------------
even = []
odd  = []

def compute(): # Function definition
  for i in range(1,30):
    if i % 2 == 0:
      even.append(i)
    else:
      odd.append(i)
compute() # Function calling
print(even)
print(odd)

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



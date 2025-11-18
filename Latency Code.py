import time
...
start = time.perf_counter()
# Your code that you want to time
end = time.perf_counter() - start
print('{:.6f}s for the calculation'.format(end)

FOR EXAMPLE :

##  Number Guessing Game : with Latency Calculation using if-elif
import time
import random 

start = time.perf_counter()

number = random.randint(1,5)
print(number)

if number == 1:
  print("Number is 1")
elif number == 2:
  print("Number is 2")
elif number == 3:
  print("Number is 3")
elif number == 4:
  print("Number is 4")
elif number == 5:
  print("Number is 5")
else :
  print("No Number")

# Your Code that you want to time
end = time.perf_counter() - start
print('{:.6f}s for the calculation'.format(end))

# DAY - 4 

## Q . Using muliple if elif concept 

score = float(input("Enter the score:  "))

if score >= 90:
  print("Grade A")
elif score >= 80:
  print("Grade B")
elif score >= 70:
  print("Grade C")
elif score >= 60:
  print("Grade D")
else:
  print("No Grade")


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



# Number Guessing Game : with Latency Calculation using if-if
import time
import random 

start = time.perf_counter()

number = random.randint(1,5)
print(number)

if number == 1:
  print("Number is 1")
if number == 2:
  print("Number is 2")
if number == 3:
  print("Number is 3")
if number == 4:
  print("Number is 4")
if number == 5:
  print("Number is 5")
else :
  print("No Number")

  
# Your Code that you want to time
end = time.perf_counter() - start
print('{:.6f}s for the calculation'.format(end))


# LOOPS : FOR LOOP & WHILE LOOP
## RANGE(start,stop,step)

for i in range(1,10,2):
  print(i)

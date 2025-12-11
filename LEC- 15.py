'''
----------------------------------------------
----------------------------------------------
# DAY - 15 :
----------------------------------------------
----------------------------------------------
'''



f = open(r'/content/demo.txt.txt',"r")
f.read()

with open('/content/demo.txt.txt', "r") as f:
  print(f.read())

with open('/content/demo.txt.txt',"w") as f:
  f.write("Enjoy Pthong programming....")

with open('/content/demo.txt.txt',"r") as f:
  print(f.readline())

with open('/content/demo.txt.txt',"r") as f:
  print(f.readline())

with open('/content/demo.txt.txt',"r") as f:
  print(f.read())

# TRY and EXCEPT BLOCK

try:
  num = float(input("Enter the first number: "))
  num1 = float(input("Enter the second number: "))

  print(num1/num)
except:
  print("Divide by Zero")
  

# Slicing a string
# string[start:stop]

string = "Hello World"
string1= "India is Great"

print(string[:5]) # o/p : Hello
print(string[:-6])  # o/p : Hello
print(string1[9:]) # o/p : Great
print(string1[-5:]) # o/p : Great

# String Slicing Example
# o/p : Ida i ra
# string1[Start:Stop:Step]
# string1= "India is Great"
print(string1[::2])
print(string1[::4])
print(string1[::-1])


# Q. Write a program to print sentence/word is palindrom or not
'''
Logic:
1. ask user to enter the string
2. store the string in variable: string
3. reverse the entered string : string1
4. use if else condition to check the palindrom or not
'''
# Step1 : Ask user to enter the string
string = input("Enter the String:")

# Step2 : Reverse the entered string: string1
string1 = string[::-1]

# Step3 : Use if else logics
if string == string1 :
  print("The Given String is Palindrom")
else:
  print("The Given String is not Palindrom")


# Q. Sagregate user based on marks
'''
Logic:
1. ask user to enter the marks and typecast to float
2.store the marks in variable: marks
3. use if else logic
'''

# Step1: Ask user to enter the marks

marks = float(input("Enter the Marks: "))

# Step2:
if marks >= 75:
  print("Bright Student")
else:
  print("Weak Student")

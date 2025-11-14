# DAY - 2 :

## SET 

a = {1,1,2,2,2,3,3,4,5,5,6}
print(a)
print(type(a))

txt = {"USA","USA",12,12,12,10,10,"India"}
print(txt)

## DICTONARY 

d = {"India" : [1,2,3,4,5],
     "USA": [10,20,30,40,50],
     "UK": [45,35,23,15,67]}
d
print(type(d))

## MATHMATICAL OPERATORS 
'''
+
-
*
/ - give output in Float / decimal
// - give output in Integer
% - give  remaindor as output
'''

print(100 * 2 / 2 + 10)
print(1000 // 2)
print(1000 / 2)
print(40 % 3)
print(20 ** 2)
print(8 ** 0.5)

## LOGICAL OPERATOR


## COMPARISON OPERATOR

print(100 <= 200) # less than or equal to
print(200 != 300) # Not equal to
print(1000 == 1000) # comparison ==

## USER DEFINED FUNCTION 
### Program :  Addition of Two Numbers

'''
1. Ask user to enter the two numbers.
2. Addition operation will be performed
3. Output will get printed.
'''
number1 = float(input("Enter the first number:"))
number2 = float(input("Enter the first number:"))

number3 = number1 + number2 

print(number3)

'''
DEFINITION 
Type Casting : Converting one data type to another
'''
## PRINT OPERATIONS
## using "F" Format Method

print(f"The addition of two numbers{number1} and {number2} is {number3}")

print(f"The addition of two numbers {number1} and {number2} is {number3}".format(number1,number2,number3))

## STRING OPERATION 

string = input("Enter a String : ")

## Concept of Indexing
'''
Logic:
H e l l o   W o r l d
0 1 2 3 4 5 6 7 8 9 10
-11           -3 -2 -1
'''
print(string[4])
print(string[-7])

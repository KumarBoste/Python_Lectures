# Single Line Comment
'''
Multi Line Comment

'''
print('Hello Python Progrmming')
print() # print function


# Data Types of Python Programming

'''
1. Integer :  int
2. Float : float
3. String : str 
4. Boolean : bool (True / False)
5. complex : complex (2 + 3i)
6. List : list []
7. Tuple : Tuple
8. Set : set
9. Dictionary : dict
10. Class : Custome Datatype
'''

# Variable Definitions
'''
1. Assignment Operator : =
2. Comparison Operator : ==
'''
# INTEGER

number = 100 # variable definition of integer value
Number = 100.28265256 # variable definition of float value
print(number==Number)

# STRING

string = " India 123" # group of characters or numbers
print(type(string))
str1 = "12345"
print(type(str1))

# BOOLEAN

a = True
b = False
c = True

print(type(a))

## using AND Logic :
print(a and b)
print(a and c)
print(b and a)
print(b and b)

## using OR Logic :
print(a or b)
print(a or c)
print(b or a)
print(b or b)

# COMPLEX NUMBER 
## complex number =  real part + imagenary part

num = 2 + 3j
print(num)
print(type(num))

# LIST : Mutable

lst = []
lst1 =[1,2,3,4.534,"India",True]
print(type(lst1))
lst2 = [1,2,3,[10,20,30],"India"]
print(type(lst2))

# TUPLE : Imutable
tup =()
tup1= (1,2,3,4.4625,"India", True)
print(type(tup1))

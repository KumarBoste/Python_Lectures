# DAY - 5 :

## Q. print th sum all even number between 1 to 50

''' 
Logic 
1. use range function to genrate even numbers betwwn 1 to 5
2. use for loop to iterate
3. Assign a Variable =  sum with "0" value and iterate n loop 

'''

sum = 0

for i in range(1,51):
  if i % 2 == 0:
    sum = sum + i
print(sum)


# USING LEN() FUNCTION : This will return toal number of characters present inside a string
len("print")


# Q . Segregate all the characters/string contains more than 6 letters/words/numbers

lst = ["India","ITvedant123","1122431436","Hackerrrrrr"]

for i in lst:
  if len(i) >= 6 :
    print(i)


# List 

 ''' 
1. DSA - Data structure
2. Mutable
'''

lst = []
lst2 =[[[[[]]]]]
lst3 = [1,2,3,4,5,6,True,False,4-7j]


# List Methods
'''
when any function defined insid a class it is called as Method
'''

a = []
print(type(a))

'''
Append : Append is use for adding the value to the end of the list.
'''

a.append(1)
print(a)
a.append([2,3,4])
print(a)
a.append(5)
print(a)

'''
Insert : add to specific value or defined value
'''
a.insert(0,0)
print(a)

'''
Pop : remove last value of list
'''
a.pop()
print(a)

'''
Remove : remove the first value which comes
'''
a.remove(0)
print(a)


a.insert(0,1)
print(a)

a.remove(1)
print(a)


'''
----------------------------------------------
----------------------------------------------
# DAY - 7 :
----------------------------------------------
-----
'''

lst3  = [[[1,2,3][4,5,6,7,8,9,10,(40,50,60)]]]
print(lst3[0[0[3[1:7]]]])


# Tuple : Immutable
a = ()
b = (([{}]))
c = (1,2,3,4,5,6,7,8,9,10)


# METHODS in Tuple
print(c.count(3))
print(c.index(3))

tup =(1,2,3)
lst = [10,11,12]
tup1 = (6,7,8)
lst1 = [13,14,15]
print(tup + tup1)
print(lst + lst1)

# LIST COMREHENSION 

lst = []

for i  in range(1,21):
  if i % 2 == 0 :
    lst.append(i)
print(lst)

# LIST COMREHENSION 

[i for i in range(1,21) if i % 2 == 0]

syntax :
[(iterator value)  for loop <condition>]


# EVEN NUMBER SQUARE :
[i**2 for i in range(1,11) if i % 2 == 0]

# DICTONARY 
d = {}


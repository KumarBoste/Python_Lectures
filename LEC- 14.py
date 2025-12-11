'''
----------------------------------------------
----------------------------------------------
# DAY - 14 :
----------------------------------------------
----------------------------------------------
'''

for i in range(1,11):
  pass
  print(i)


for i in range(1,11):
  continue
  print(i)


for i in range(1,11):
  break
  print(i)

for i in range(1,5):
  pass
  for j in range(1,5):
    print(j)

for i in range(1,5):
  pass
  for j in range(1,5):
    print(j,end = ' ')


for i in range(1,6):
  pass
  for j in range(1,6):
    continue
    print("Hello")


for i in range(1,3):
  continue
  for j in range(1,4):
    pass
    for k in range(1,4):
      print(k)

for i in range(1,3):
  pass
  for j in range(1,4):
    pass
    for k in range(1,4):
      print(k)


import logging
logging.basicConfig(level = logging.INFO,
                    filemode = 'w',
                    filename = 'model.log',
                    format = '%(asctime)s - %(message)s',
                    force = True
                    )

logging.info("Hello World")

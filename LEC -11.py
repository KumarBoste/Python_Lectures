'''
----------------------------------------------
----------------------------------------------
# DAY - 11 :
----------------------------------------------
----------------------------------------------
'''

# class 
class car:

  # Constructor / Special Function

  def __init__(self,no_of_door,no_of_wheels):
    self.no_of_door = no_of_door  # Feature 1
    self.no_of_wheels = no_of_wheels # Feature 2

  # Method of class : Car
  def mileage(self,km):
    self.km =km
    return self.km + 100


  # method of class : car

  def features(self):
    print("No of door: ", self.no_of_door)  # Accessing feature 1
    print("No of wheels: ", self.no_of_wheels)  # Accessing Feature 1

a = car (5,7)
print(a.mileage(4))

a.features()


# EXAMPLE:
class car:
  def __init__(self,mileage,km,color,bodytype):
    self.mileage = mileage
    self.km = km
    self.color = color
    self.bodytype =bodytype

  def mileage_car (self,mileage):
    self.mileage = mileage
    return self.mileage + 40

object = car(30,40,"Red","Sedan")
print(object.km)
object.mileage_car(30)

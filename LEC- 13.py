'''
----------------------------------------------
----------------------------------------------
# DAY - 13 :
----------------------------------------------
----------------------------------------------
'''

import time
start = time.perf_counter()
class MovieBooking:
    def __init__(self, owner, pin, seats, price):
        self.owner = owner          # public attribute
        self.__pin = pin            # private attribute
        self.__seats = seats        # private attribute
        self.__price = price        # private attribute

    # Private method to verify pin
    def __verify_pin(self, pin):
        return pin == self.__pin

    # Public method – Show available movies
    def show_movies(self):
        return (
            "Available Movies:\n"
            "1. Avengers: Endgame\n"
            "2. Avatar: The Way of Water\n"
            "3. Joker\n"
            "4. Oppenheimer"
        )

    # Public method – Check total cost
    def check_cost(self, pin):
        if self.__verify_pin(pin):
            return f"Total Cost: {self.__seats * self.__price}"
        return "Invalid PIN!"

    # Public method – Change booked seats
    def update_seats(self, pin, new_seat_count):
        if not self.__verify_pin(pin):
            return "Invalid PIN!"

        if new_seat_count > 0:
            self.__seats = new_seat_count
            return f"Seats updated to {self.__seats}."
        return "Invalid seat number."

    # Public method – Book movie
    def book_movie(self, pin, movie_choice):
        if not self.__verify_pin(pin):
            return "Invalid PIN!"

        movies = {
            1: "Avengers: Endgame",
            2: "Avatar: The Way of Water",
            3: "Joker",
            4: "Oppenheimer"
        }

        if movie_choice in movies:
            return f"Booking Confirmed for '{movies[movie_choice]}' | Seats: {self.__seats} | Total Price: {self.__seats * self.__price}"

        return "Invalid movie selection."


# Test Case
booking = MovieBooking("Sujal", pin=1234, seats=2, price=150)

print(booking.show_movies())
print(booking.check_cost(1234))
print(booking.book_movie(1234, 3))
print(booking.update_seats(1234, 4))
print(booking.book_movie(1111, 2))  # wrong pin test


# Your code that you want to time
end = time.perf_counter() - start
print('{:6f}s for the calculation '.format(end))



class Product:

  # Constructor
  def __init__(self,id):
    self.id = id
  # Product Details using Method
  def Product_Details(self):
        self.name = input("Enter Product Name: ")
        self.price = float(input("Enter Product Price: "))
        self.qty = int(input("Enter Product Quantity: "))

  # Method to Display
  def Display(self):
    print("Product Id:",self.id)
    print("Product Name:",self.name)
    print("Product Price:",self.price)
    print("Product Quantity:",self.qty)

p1 = Product(101)

p1.Product_Details()
p1.Display()



 # inheritances

import time
start = time.perf_counter()
class BankAccount:


   def __init__(self ,owner ,balance=0):
    self.owner = owner
    self.balance = balance

   def deposits(self,amount):
    self.balance += amount
    print(f"Deposit Amount:{amount}")

   def withdraw(self,amount):
    if amount <= self.balance:
      self.balance -= amount
      print(f"Withdraw Amount: {amount}")
    else:
      print(f"Insufficient funds!")


   def get_balance(self):
    return self.balance

class SavingsAccount(BankAccount):

   def __init__(self,owner, balance=0, interest_rate=0.05):
    super().__init__(owner, balance)
    self.interest_rate = interest_rate

   def add_interest(self):
    interest = self.balance * self.interest_rate
    self.balance += interest
    print(f"Interest Added: {interest}")

class CurrentAccount(BankAccount):

  def __init__(self,owner,balance=0, overdraft_limit=1000):
    super().__init__(owner,balance)
    self.overdraft_limit = overdraft_limit

  def withdraw(self,amount):
    if amount <= self.balance + self.overdraft_limit:
      self.balance -= amount
      print(f"Withdrawn using overdraft : {amount}")
    else:
      print("Exceeded overdraft limit!")


s = SavingsAccount("Sujal", 2000)
s.add_interest()
print("Saving Balance:", s.get_balance())

c = CurrentAccount("Sujal",1000)
c.withdraw(1500)
print("Current Balance:", c.get_balance())

# Your code that you want to time
end = time.perf_counter() - start
print('{:6f}s for the calculation '.format(end))


# class is a custom datatype
import time
start = time.perf_counter()
class MovieBooking:

  # Constructor
  def __init__ (self,owner,pin,price,seat,movie_name):
    self.owner = owner
    self.__pin = pin
    self.price = price
    self.seat = seat
    self.movie_name = movie_name

  def __verify_pin(self,pin):
    return pin == self.__pin # Comparision

  def book_seats(self,pin, new_seat_count):
    if not self.__verify_pin(pin):
      return f"Invalid Pin!"

    if new_seat_count > 0:

            # Only add this check (because your code would break)
            if new_seat_count > self.seat:
                return "Seats are not Available!"

            # SAME logic: Deduct seats
            self.seat -= new_seat_count

            # NEW: total price
            total_price = new_seat_count * self.price

            return (
                f"Movie: {self.movie_name}\n"
                f"Booked Seats: {new_seat_count}\n"
                f"Total Price: ₹{total_price}\n"
                f"Available Seats: {self.seat}")


class KGF(MovieBooking):
  def __init__ (self,owner,pin,price,seat,movie_name):
    super().__init__ (owner,pin,price,seat,movie_name)

class RRR(MovieBooking):
  def __init__ (self,owner,pin,price,seat,movie_name):
    super().__init__ (owner,pin,price,seat,movie_name)

class Jawan(MovieBooking):
  def __init__ (self,owner,pin,price,seat,movie_name):
    super().__init__ (owner,pin,price,seat,movie_name)


kgf = KGF("Sujal", 2252, price=200, seat=50, movie_name="KGF")
print(kgf.book_seats(2252, 3))

rrr = RRR("Sujal",2252,price = 150,seat =40,movie_name = "RRR")
print(rrr.book_seats(2252,5))
# Your code that you want to time
end = time.perf_counter() - start
print('{:6f}s for the calculation '.format(end))


# polymorphism enables to write more flexible and reusable code

class Bird:
  def sound(self):
    return "Tweet"

class Dog:
  def sound(self):
    return "Bark"

def make_sound(animal):
    print(animal.sound())

# create objects
bird = Bird()
dog = Dog()

# same function call, different class
make_sound(bird)
make_sound(dog)




# define parent class
class Parent:
  # Define Special Method : Constructors
  def __init__(self,feature1,feature2):
    self.feature1 = feature1
    self.feature2 = feature2
  # Define instance method : method
  def sound(self):
    return "Woow"
# Define child class
class Child1(Parent):
  def __init__(self,feature1,feature2):
    super().__init__(feature1,feature2)

    print(self.feature1)
# Define Method
  def sound(self):
    return super().sound()

# Define child class
class Child2(Parent):
  def __init__(self,feature1,feature2):
    super().__init__(feature1,feature2)

    print(self.feature1)
# define method
  def sound(self):
    return "Grrrrr"

obj = Child1(100,200)
obj1 =obj.sound()
obj2 = Child2(100,200)
obj3 =obj2.sound()

print(obj1)
print(obj3)












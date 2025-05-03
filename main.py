# QUESTION 1

class Student:
    def __init__(self,name,marks):
        self.name = name
        self.marks = marks

    def display(self):
        print(f"Name: {self.name} , Marks: {self.marks}")

details = Student("Soban",90)
details.display()


# Question 2

class Counter:
    count = 0

    def __init__(self):
        Counter.count += 1

    @classmethod
    def display_count(cls):
        print(f"Total objects created: {cls.count}")

a = Counter()
b = Counter()
c = Counter()
d = Counter()
e = Counter()

Counter.display_count()



# QUESTION 3

class Car:
    def __init__(self,brand):
        self.brand = brand

    def start(self):
        print(f"{self.brand} car has been started")

car_name = Car("Toyota")
car_name.start()


# QUESTION 4

class Bank:
    bank_name = "Al-Habib Bank"

    @classmethod
    def change_bank_name(cls, name):
        cls.bank_name = name

b1 = Bank()
b2 = Bank()
Bank.change_bank_name("Islamic Bank")
print(b1.bank_name)


# QUESTION 5

class MathUtlis:
    @staticmethod
    def add(a,b):
        return a + b
    
print(MathUtlis.add(5,5))


# QUESTION 6

class Logger:
    def __init__(self):
        print("Logger started")

    def __del__(self):
        print("Logger Destroyed")

log = Logger()
del log


# QUESTION 7

class Employee:
    def __init__(self,name,salary,ssn):
        self.name = name   # public
        self._salary = salary  # protected
        self.__ssn = ssn    # private
    
emp = Employee("John", 50000, "123-45-6789")
print(emp.name)          # Accessible
print(emp._salary)       # Accessible, but discouraged
# print(emp.__ssn)       # Error: private
print(emp._Employee__ssn)  # Accessible with name mangling


# QUESTION 8

class Person:
    def __init__(self,name):
        self.name = name

class Teacher(Person):
    def __init__(self,name,subject):
        super().__init__(name)
        self.subject = subject

call = Teacher("Jones", "English")
print(call.name,call.subject)



# QUESTION 9

from abc import ABC , abstractmethod

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

class Rectangle(Shape):
    def __init__(self,width,height):
        self.width = width
        self.height = height
    def area(self):
        return self.width * self.height
    
square = Rectangle(5,5)
print(square.area())


# QUESTION 10

class Dog:
    def __init__(self,name,breed):
        self.name = name
        self.breed = breed

    def bark(self):
        print(f"{self.name} is barking ")

animal = Dog("German Shepard","rex")
animal.bark()


# QUESTION 11

class Book:
    total_books = 0

    @classmethod
    def increment_book_count(cls):
        cls.total_books += 1

Book.increment_book_count()
Book.increment_book_count()
Book.increment_book_count()
print(Book.total_books)



# Question 12

class TemperatureConvertor:
    @staticmethod
    def celsius_to_fahrenheit(c):
        return (c * 9/5) + 32

print(TemperatureConvertor.celsius_to_fahrenheit(2))


# QUESTION 13

class Engine:
    def start(self):
        print("Engine has started")

class Car:
    def __init__(self,engine):
        self.engine = engine

    def start(self):
        self.engine.start()

e = Engine()
c = Car(e)
c.start()


# QUESTION 14

class Employee:
    def __init__(self,name):
        self.name = name
    
class Department:
    def __init__(self,employee):
        self.employee = employee

emp = Employee("Alex")
dep = Department(emp)
print(dep.employee.name)


# QUESTION 15

class A:
    def show(self):
        print("A")

class B(A):
    def show(self):
        print("B")

class C(A):
    def show(self):
        print("C")

class D(B,C):
    pass

d = D()
d.show()  # Outputs B due to MRO(Method Resolution Order (MRO))


# QUESTION 16

def log_function_call(func):
    def wrapper():
        print("Function is being called")
        return func()
    return wrapper

@log_function_call
def say_hello():
    print("Hello")

say_hello()




# QUESTION 17

def add_greeting(cls):
    cls.greet = lambda self: "Hello from Decorator!"
    return cls

@add_greeting
class Person:
    def __init__(self,name):
        self.name = name

p = Person("Alexander")
print(p.greet())


# QUESTION 18

class Product:
    def __init__(self,price):
        self._price = price

    @property
    def price(self):
        return self._price
    
    @price.setter
    def price(self,value):
        self._price = value

    @price.deleter
    def price(self):
       del self._price

p = Product(100)
print(p.price)
p.price = 200
print(p.price)
del p.price


# QUESTION 19

class Multiplier:
    def __init__(self,factor):
        self.factor = factor
    
    def __call__(self,value):
        return self.factor * value
    
m = Multiplier(5)
print(callable(m))
print(m(10))

# QUESTION 20

class InvalidAgeError(Exception):
    pass

def check_age(age):
    if age < 18:
        raise InvalidAgeError("Age must be atleast 18")
    print("Age is Valid")

try:
    check_age(16)
except InvalidAgeError as e:
    print(e)


# QUESTION 21
class Countdown:
    def __init__(self, start):
        self.current = start

    def __iter__(self):
        return self

    def __next__(self):
        if self.current < 0:
            raise StopIteration
        val = self.current
        self.current -= 1
        return val

for num in Countdown(5):
    print(num)

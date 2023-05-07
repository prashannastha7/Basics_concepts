# First Basics
"""class Student:
    pass


Ram = Student()
Sita = Student()

Ram.name = "Ram"
Ram.std = 10
Sita.std = 9
Sita.subject = ["Nepali", "Japanese"]
print(Ram.std, Sita.subject)

#instance and class variable
class Employees:
    no_of_leaves = 9
    pass

harry = Employees()
larry = Employees()

harry.name= "Harry"
harry.salary = 4456

larry.name = "Larry"
larry.salary = 4896
print(harry.no_of_leaves)
Employees.no_of_leaves = 5 #class variable so only employees. can change for both
print(larry.no_of_leaves)
harry.no_of_leaves = 63  #harry and larry are instances can't change class variable
print(larry.no_of_leaves)"""

# Self & init(constructor)
"""class Employees:
    def printdetails(self): #self means jo le call garyoo teii huncha self means instances pass
        return f"Name is {self.name}. Salary is {self.salary}.."  #f -> fstring used garda data conversion garirakhnu 
        #pardaina contentaion easily..

rohan = Employees()
rohan.name = "Rohan"
rohan.salary = 45895
print(rohan.printdetails())

#init is constructor used to passed argument

class Employees:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

Pras = Employees("Prashanna", "7895200")
print(Pras.salary)"""

# Class_methods
"""#Self chahidaina class chahincha insta can also access then class methods
#A class method is a method that is bound to a class rather than its object. It doesn't require creation of a class 
#instance, much like staticmethod.
#Like a static method, a class method doesn’t need an object to be instantiated.
#A class method differs from a static method in that a static method doesn’t know about the class itself. 
#In a classmethod, the parameter is always the class itself.

class Employee:
    no_of_leaves = 9

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    @classmethod   # try commenting this line
    def change_leaves(cls, newleaves):
        cls.no_of_leaves = newleaves


harry = Employee("Harry", 255)
larry = Employee("Larry", 255)

larry.change_leaves(34)
print(harry.no_of_leaves)"""

# clasmethods as alternative constructors
"""class Employee:
    no_of_leaves = 9

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    @classmethod   # try commenting this line
    def change_leaves(cls, newleaves):
        cls.no_of_leaves = newleaves

    @classmethod
    def from_dash(cls, string):  #cls- class
        return cls(*string.split("-"))


harry = Employee("Harry", 255)
karan = Employee.from_dash("Karan-450")

print(karan.salary)"""

# Static Methods(neither instance nor class)
"""class Employee:
    no_of_leaves = 9

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    @classmethod  # try commenting this line
    def change_leaves(cls, newleaves):
        cls.no_of_leaves = newleaves

    @classmethod
    def from_dash(cls, string):  # cls- class
        return cls(*string.split("-"))

    @staticmethod
    def prints(string):
        print("This is good" + string)
        return 69  # without return it print None in output


harry = Employee("Harry", 255)
karan = Employee.from_dash("Karan-450")

print(karan.prints("Boy"))"""

# Single Inheritance
"""class Employee:
    no_of_leaves = 9

    def __init__(self, aname, salary, role):
        self.name = aname
        self.salary = salary
        self.role = role

    def printdetails(self):
        return f"Name is {self.name}. Salary is {self.salary} and role is {self.role}"

    @classmethod
    def change_leaves(cls, newleaves):
        cls.no_of_leaves = newleaves

    @classmethod
    def from_dash(cls, string):  # cls- class
        return cls(*string.split("-"))

    @staticmethod
    def prints(string):
        print("This is good" + string)
        return 69

class Programmer (Employee):
    def __init__(self, aname, salary, role, languages):
        self.name = aname
        self.salary = salary
        self.role = role
        self.language = languages

    def printprog(self):
        return f"The Programmer's Name is {self.name}. Salary is {self.salary}, role is {self.role} & languages are {self.language} .."


harry = Employee("Harry", 255, "Instructor")
karan = Employee("Karan", 255, "Student")
ram = Programmer("Ram", 555, "Programmer", ["Python"])

print(ram.printprog())
print(ram.printdetails())  # access of Employees"""

# Multiple inheritance
"""class Employee:
    no_of_leaves = 9
    var = 8

    def __init__(self, aname, salary, role):
        self.name = aname
        self.salary = salary
        self.role = role

    def printdetails(self):
        return f"Name is {self.name}. Salary is {self.salary} and role is {self.role}"

    @classmethod
    def change_leaves(cls, newleaves):
        cls.no_of_leaves = newleaves

    @classmethod
    def from_dash(cls, string):  # cls- class
        return cls(*string.split("-"))

    @staticmethod
    def prints(string):
        print("This is good" + string)


class Player:
    var = 9
    no_of_games: 5

    def __init__(self, name, game):
        self.name = name
        self.game = game

    def printdetails(self):
        return f"Name is {self.name}. Game is {self.game}."


# jun aagadi cha tho matra inheritance garcha
class Programmer(Employee, Player):  # order matters emp and pla see last
    # var = 10
    language = "C++"

    def printlanguage(self):
        print(self.language)


harry = Employee("Harry", 255, "Instructor")
karan = Employee("Karan", 255, "Student")

ram = Player("Ram", "Football")
Hari = Programmer("Hari", 2500,
                  "Coolprog")  # inheritance garda employee suru ma cha so suru ma empl ko constructor hercha
# Hari = Programmer("Hari" , "Football") # if pla aagadi aani emp vako vaya
print(Hari.printdetails())
print(Hari.printlanguage())
print(Hari.var)  # if suru ma pla aani emp vako vaya var 9 aauthiyo"""

# Multilevel inheritance
"""class Dad:
    Football = "Level 4"

class Son(Dad):
    #Football = "Level 5"
    Basketball = "Level 3"
    Guitar = "Level 2"

class Grandson(Son):
    pass

Ram = Dad()
Hari = Son()
Ramu = Grandson()

print(Ramu.Football)
print(Ramu.Basketball)"""

# Private public protected
"""class Employees:
    _protec = 9  # class ma access huncha aani derived class ma pani milcha
    __private = 965 #derived ma access didaina only class and also use name mangling
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def printdetails(self):
        return f"Name is {self.name}. Salary is {self.salary}.."

Pras = Employees("Prashanna", "7895200")
print(Pras._Employees__private) # to access private use name mangling to make complex to use
print(Pras._protec)"""

# Super()
"""# when two constructor is use and second one overwrite the first constructor we cann't access first one so Super() is
# used to acces the first one.

class A:
    classvar1 = "I am a class variable in class A"

    def __init__(self):
        self.var1 = "I am inside class A's constructor"
        self.classvar1 = "Instance var in class A."
        self.special = "special"

class B(A):
    classvar1 = "I am class B"

    def __init__(self):
        #super().__init__()  # useto accessclassA.initpaila call cha so classA run vayaraferi classAlaiBle replacegarcha
        self.var1 = "I am inside class B's constructor"
        self.classvar1 = "Instance var in class B." # yesto garda class A ko ins run hudaina becoz overwrite vaisakiyo
        super().__init__() # yesma pasi balla init call cha so class A run huncha in last print 
        print(super().classvar1)

a = A()
b = B()

print(b.special, b.var1, b.classvar1)"""

# Diamond problem Multiple
"""class A:
    def met(self):
        print("This is method from class A")

class B(A):
    def met(self):
        print("This is method from class B")

class C(A):
    pass
    # def met(self):
    #     print("This is method from class C")

class D(C,B):  #try (B,C)
    pass

a = A()
b = B()
c = C()
d = D()

d.met()"""

# Operator overloading and Dunder method
"""class Employee:
    no_of_leaves = 9

    def __init__(self, aname, salary, role):
        self.name = aname
        self.salary = salary
        self.role = role

    def printdetails(self):
        return f"Name is {self.name}. Salary is {self.salary} and role is {self.role}"

    @classmethod
    def change_leaves(cls, newleaves):
        cls.no_of_leaves = newleaves

    def __add__(self, other):  #Dunder
        return self.salary + other.salary

    def __truediv__(self, other):   # Mapping operators to Functions
        return self.salary / other.salary

    def __repr__(self):
        return f"Employee('{self.name}', '{self.salary}', '{self.role}')"

emp1 = Employee("Ram", 500, "Programmer")
emp2 = Employee("Ham", 300, "Designer")
print(emp1 + emp2)
print(emp1)  #repr ko ho """

# Abstract Base class
"""# used to make sure that derived class contain things mandotary that we want to

from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def printarea(self):
        return 0


class Rectangle(Shape):

    def __init__(self):
        self.length = 6
        self.breadth = 4

    def printarea(self):   #try commenting this functions(2line)
        return self.length * self.breadth


rect1 = Rectangle()
print(rect1.printarea())"""

#Setter

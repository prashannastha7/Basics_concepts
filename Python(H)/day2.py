# 11. FOR_LOOPS - is used to iterate over sequence, which could be list,tup arr or stg
"""
# syntax-> For counter in sequence:
#          statements
# eg:
# X = [1,2,3,'simple']
# print (X[0], X[1], X[2]) if there is 1000 items it will be hard so use for
# for i in X:
#   print(X)

list1 = ["Harry", "Carry", "Larry", "Marry"]
list2 = [["Harry", 1], ["Carry", 2], ["Larry", 3], ["Marry", 6]]
for item in list1:
    print(item)
print(list1[0:5])
for item, lol in list2:
    print(item, "and lolly is", lol)

X = "Hey there, how"
    for i in x :
    print (i),end="" #try without end
# To sum using for loop
b = [20, 15, 5]
total = 0
for e in b:
    total = total + e
print(total)

# To write number 1 to 100 we use range()
c = list(range(1, 101))
print(c)
for i in range(1, 6):
    print(i)

#sum
sum = 0
for i in range(0,21):
   if i%2==0:
      sum=sum+i
print(sum)

#pattern
n = int(input("Enter your number: "))
for i in range(1,n+1) :
    for j in range(1, i):
       print(j,end'')
    print()

# matrix sum
r = int(input("Enter number of rows "))
c = int(input("Enter number of columns "))
X = []
val = []
for i in range(0, r):  # this outer for loop for the element in x
    for j in range(0, c):  # this inner for loop for between the element in x
        val.insert(j, int(input("Enter the %d * %d element " % (i, j))))
    X.insert(i, val)
    val = []
Y = []
for i in range(0, r):
    for j in range(0, c):
        val.insert(j, int(input("Enter the %d * %d element" % (i, j))))
    Y.insert(i, val)
    val = []
Sum = []

for i in range(0, r):
    for j in range(0, c):
        val.insert(j, X[i][j] + Y[i][j])
    Sum.insert(i, val)
    val = []
print(Sum)"""

# . Quiz3
"""lists = [1, 2, 6, 8, 9, "Ram", "Jax"]
for list in lists:
    if str(list).isnumeric() and list>6:
        print(list)"""

# 12. WhileLoop is used to repeat a section of code unknown number of times until cond is met
"""i = 0
while i < 4:
    print(i)
    i += 1
    
i = 0
while i < 20:
    print(i + 1, end=" ")
    i += 1
    
#sum of natural number 
i = 1
sum = 0
while i<10 :
    sum = sum + i
    i+=1
print(sum)    

#pattern

n= int(input("Enter a number"))
i = 1
while i<=n :
      j = 1
      while j<=1
         print(i, end='')
         j+=1
      i+=1
      print()   

#using for
total = 0
for i in range(1, 5):
    total += i
    print(total)
#using while
total1 = 0
j = 1
while j < 5:
    total1 += j
    j += 1
print(total1)"""

# 13. Break&Continue
"""i = 0
while True:
    print(i, end=" ")
    if i == 20:
        break
    i += 1

i = 0
while True:
    if i < 5:
        i += 1
        continue
    print(i, end=" ")
    if i== 20:
        break
    i = i+1
"""

# Quiz4
"""while True:
    num = int(input("Enter a number:  \n"))
    if num > 100:
        print("Congratulation")
        break
    else:
        print("Try again")
        continue"""

# 14. Guess the number
"""p = 69
i = 5
while True:
    guess = int(input("Enter the number:  \n"))
    if guess > p:
        print("guess smaller")
        print("You have now ", i - 1, " lives left")
        i -= 1
    elif guess == p:
        print("You are right ")
        break
    else:
        print("Guess larger")
"""

"""n=18
number_of_guesses=1
print("Number of guesses is limited to only 9 times: ")
while (number_of_guesses<=9):
    guess_number = int(input("Guess the number :\n"))
    if guess_number<18:
        print("you enter less number please input greater number.\n")
    elif guess_number>18:
        print("you enter greater number please input smaller number.\n ")
    else:
        print("you won\n")
        print(number_of_guesses,"no.of guesses he took to finish.")
        break
    print(9-number_of_guesses,"no. of guesses left")
    number_of_guesses = number_of_guesses + 1

if(number_of_guesses>9):
    print("Game Over")
    
#Guess number .2
import random
nump = random.randint(1000,9999)
n = int(input("Enter a 4 digit number"))
while n!=10 :
    num = nump
    cor = 0
    while num % 10:
        numc = num %10
        nc = n%10
        num = num//10
        n = n//10
        if numc==nc;
           cor=cor+1
    if cor == 4:
       print("congratulations....")
       break
    else :
       print("%d digits were guessed right" %cor)
       n = int(input("Enter a 4 digit number"))
else :
print("You quit the game")   """

# Array-> it only take one dimensional array

"""from array import *

arr = array('i', [-1, 2, 3, 4, 5])
print(arr)
print(arr[2])
for i in arr:  # in range(4)
    print(i)

arr.append(10)
arr.reverse()
arr.remove(2)
print(arr)

Arr = array("i", [])
x = int(input("Enter size of array "))
print("Enter %d element" % x)
for i in range(x):
    n = int(input())
    arr.append(n)
print(arr)"""

# 15. Membership Operator
"""lis = [1, 2, 58, 69, 85]
print(69 in lis)
print(87 not in lis)"""

# 16. Function
""" SYNTAX
def function_name():
    statement(s)

def welcome():
    print("Good morning")

welcome()    

a = 9
b = 8
c = sum(a, b)  # ctrl + then sum click # built in function

# User defined
# 1. Without argument and return
def function1():
    print("Hello you're in function")
(function1())
(function1())
(function1())

# 2. With argument
def function2(a, b):
    print("Hello you're in function", a+b)
(function2(5, 7))


def function3(c, d):
    average = (c+d)/2
    print(average)

v = function3(5, 7)
print(v)

# 3. With both 
def function3(c, d):
    average = (c+d)/2
    return (average)

v = function3(5, 7)
print(v)"""

# Docstring in Function -> used to see comment in output mainly used by programmer to aware in veryy veryy large program
# def function3(c, d):
#     """This is a function which will calculated it does not work for 3 numbers..."""
#     average = (c + d) / 2
#     return (average)
#
#
# v = function3(5, 7)
# print(v)
# print(function3.__doc__)

# Try except exception -> used to print down operation even front operation does not executed.
"""print("Enter num1")
num1 = input()
print("Enter num2")
num2 = input()
try:
    print("The sum is ",
          int(num1) + int(num2))
except Exception as e:
    print(e)

print("This is me ")"""

# EXTRA
"""def add(*a):
    total = 0
    for i in a:
        total += i
    print("The sum is ", total)


add(10, 20, 30, 50)

print("pass by value")


def add(a, b):
    print(id(a))  # address of a
    a = 2
    b = 3
    total = a + b
    print("Sum is ", total)


x = 10
y = 20
add(x, y)
print("Sum is ", x + y)

print('Pass by reference ')
def hello(k):
    k[0] = 12
    print(k)
    return

j = [1, 2, 3, 4]
hello(j)
print(j)"""

# OOP
"""class Person:

    def __init__(self):
        self.name = "Pras"
        # self.gender = g
        # self.age = a

    def talk(self):
        print("Hi I'm", self.name)


obj = Person()
obj.talk()  # Person.talk(obj)


class Person:

    def __init__(self, n, g, a):
        self.name = n
        self.gender = g
        self.age = a

    def talk(self):
        print("Hi I'm ", self.name)

    def vote(self):
        if self.age < 18:
            print("I am not eligible to vote")
        else:
            print("I am eligible")


obj = Person("Pras", "Male", 18)
obj2 = Person("prashanna", "Male", 22)
obj.talk()
obj.vote()

obj2.talk()
obj2.vote()


class car:
    def __init__(self, year, speed):
        self.year = year
        self.speed = speed

    def getspeed(self):
        print("Max speed is ", self.speed)

    def setspeed(self, speed):
        self.speed = speed


BMW = car(2018, 155)
FORD = car(2015, 169)
BMW.getspeed()
BMW.setspeed(145)
BMW.getspeed()
FORD.getspeed()


# inheritance
class Sedan(car):  # child class
    def accelerate(self):
        print("137")

    def openTrunk(self):
        print("Trunk has been opened")


class SUV(car):
    def accelerate(self):
        print("127")


Honda = Sedan(2018, 150)
BMW.getspeed()
Honda.getspeed()
Honda.openTrunk()"""

# Thread : A sequence of instruction in a program that can be executed independently of the remaining program
"""from threading import *



def show():
    print("This is child thread")


t = Thread(target=show())  # creating thread
t.start()
print("This is parent thread")


class MyThread(Thread):
    def run(self):
        for j in range(5):
            print("\nThis is a child class")


t = MyThread()
t.start()
for j in range(5):
    print("\nThis is the main thread")

class Demo:
    def show(self):
        for i in range (5):
            print("This is the child thread.")
obj = Demo()
t = Thread(target=obj.show())
t.start()
for i in range(5):
    print("This is parent thread")"""

#multithreading
"""from threading import *
class Demo:
    def num(self):
        for i in range(1, 6):
            print("The number is ",i)

    def double(self):
        for i in range(1, 6):
            print("The double of number is ", 2*i)

    def square(self):
        for i in range(1, 6):
            print("The square number is ", i*i)

obj=Demo()
t1=Thread(target=obj.num)
t2=Thread(target=obj.double)
t3=Thread(target=obj.square)

t1.start()
t2.start()
t3.start()

t1.join()
t2.join()
t3.join()

print("This is the main thread")

#correction
import time
class Demo:
    def num(self):
        for i in range(1, 6):
            print("The number is ",i)

    def double(self):
        for i in range(1, 6):
            print("The double of number is ", 2*i)


    def square(self):
        for i in range(1, 6):
            print("The square number is ", i*i)
          

obj=Demo()
t1=Thread(target=obj.num)
t2=Thread(target=obj.double)
t3=Thread(target=obj.square)

t1.start()
time.sleep(0.2)
t2.start()
time.sleep(0.2)
t3.start()


t1.join()
t2.join()
t3.join()

print("This is the main thread")

import time
class Demo:
    def num(self):
        for i in range(1, 6):
            print("The number is ",i)
            time.sleep(1)

    def double(self):
        for i in range(1, 6):
            print("The double of number is ", 2*i)
            time.sleep(1)

    def square(self):
        for i in range(1, 6):
            print("The square number is ", i*i)
            time.sleep(1)

obj=Demo()
t1=Thread(target=obj.num)
t2=Thread(target=obj.double)
t3=Thread(target=obj.square)

t1.start()
time.sleep(0.2)
t2.start()
time.sleep(0.2)
t3.start()


t1.join()
t2.join()
t3.join()

print("This is the main thread")"""
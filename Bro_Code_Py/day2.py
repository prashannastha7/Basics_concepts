#Function
'''def hello(name, age):
    print("Hello "+ name)
    print("you are " + str(age) + " years old")
hello("Prashanna", 21)

def multiply(num1 , num2):
    result = num1 * num2
    return result

print(multiply(5,5))

#Keyword arguments -> order doesn't matter python knows name of argument

def hello(first,middle,last):
    print("Hello " + first + " "+ middle+ " " + last)

hello(last = "Stha", middle= "Bdr", first="Prashanna")
'''

# *args -> parameter that will pack all arguments into a tuple useful so that a function can accept a varying amount of parameters.
'''#argument jati ota pani pass garna milcha
# **kwargs -> parameter that will pack all arguments into a dictionary
def funargs(normal, *args, **kwargs):
    print(normal)
    for item in args:
        print(item)
    print("\n I would like to introduce ")
    for key, value in kwargs.items():
        print(f"{key} is a {value}")

name= ["Ram", "Hari", "Pras","Programmer"]
normal = "I am a normal"
kw = {"Ram": "Monitor", "Hari": "Pilot", "Pras": "Fitness"}
funargs(normal, *name, **kw)'''

#random
'''import random

x = random.randint(1,6)
y = random.random()

mylist = ['rocks', 'scissors', 'paper']
z = random.choice(mylist)

print(z)
cards = [1,2,3,4,5,6,7,'A','K','Q','J']
random.shuffle(cards)
print(cards)'''

# exception =   events detected during execution that interrupt the flow of a program
'''try:
    numerator = int(input("Enter a number to divide: "))
    denominator = int(input("Enter a number to divide by: "))
    result = numerator / denominator
except ZeroDivisionError as e:
    print(e)
    print("You can't divide by zero! idiot!")
except ValueError as e:
    print(e)
    print("Enter only numbers plz")
except Exception as e:
    print(e)
    print("something went wrong :(")
else:
    print(result)'''

#File detection
'''import os

path = "C:\\Users\\User\\Desktop\\test.txt"

if os.path.exists(path):
    print("That location exists!")
    if os.path.isfile(path):
        print("That is a file")
    elif os.path.isdir(path):
        print("That is a directory!") #if in  folder
else:
    print("That location doesn't exist!")'''

#modules
'''import message as msg
#from message import * 

msg.hello()
msg.bye()'''

#lambda function = function written in 1 line using lambda keyword
''''#lambda parameter: expression

double = lambda x:x*2
multiply = lambda x, y:x * y
full_name = lambda first_name, last_name: first_name+" "+ last_name
age_check = lambda age: True if age >=18 else False

print(multiply(5, 6))
print(age_check(15))
print(full_name("Prashanna", "Shrestha"))
'''

#if__name__ = '__main__': -> type main aafai aaucha
#euta file name hello aarko file ma import hello garda hello ma vako sabai run hunchaa usta so
# use this is__name aani tesko vitra function call garyo vaney aarko file ma
# run hudaina

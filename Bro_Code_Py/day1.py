#Shorcuts
'''ctrl + D : copy mathi ko tala
alt + D : select same words
ctrl + backspace : delete words'''

#basics
''' first_name = "Prashanna "
last_name = "Shrestha"
full_name = first_name + last_name
print(type(first_name))
print("Hello " + full_name)

age = 21
#print("your age is:" + age) #this is error
print("Your age is: " + str(age))

name, age, attractive = "Bro", 21, True
Sus = ag = hu = 30
print(ag)
print(name, age)
#print(age)
print(attractive)'''

#String method
'''name = "RamR"
print(len(name))
print(name.find("R"))
print(name.isalpha())
print(name.count("R"))
print(name.replace("R","s"))

#Type casting
x = 3
print(x*3)
print(str(x)*3)
print("The value of X is " + str(x)) 

name = input("What is your name? : ")
age = int(input("How old are you?: "))
print("Hello "+ name)
age = age + 1
print("You are " + str(age) + " years old")'''

#F string -> fast than other
'''val = 'Geeks'
print(f"{val}for{val} is a portal for {val}.")

name = 'Tushar'
age = 23
print(f"Hello, My name is {name} and I'm {age} years old.")'''

#math func
'''import math

pi = 3.14
a = -5
x = 1
y = 2
z = 3

print(round(pi))
print(math.ceil(pi))
print(math.floor(pi))
print(abs(a))
print(pow(pi,2))
print(math.sqrt(64))
print(max(x,y,z))'''

#Slicing -> [Start:Stop:Step]
'''name = "Prashanna"
nam = name[0:3]
na= name[0:9:2]
names= name[::-1]
print(names)'''

#Loops
''''#while loop

name = ''
while len(name) == 0:
    name = input("Enter your name: ")

print("Hello " + name)

#For loop -> limited time
import time
for i in range(10,20):
    print(i)

for i in range(10,20,2):
    print(i)

for second in range(10,0,-1):
    print(second)
    time.sleep(1)
print("   Nhu daya bhintuna!!!")

#Nested Loop = The inner loop will finish all of it's iteration before
#              finishing one iteration of the outer loop

rows = int(input("Enter rows: "))
columns = int(input("Enter columns: "))
symbol = input("Enter a symbol to use: ")

for i in range(rows):
    for j in range(columns):
        print(symbol, end="")
    print()
'''

#Lists -> used to store multiple items in a single variable
'''food = ["Pizza", "Ham", "Momo", "Rice"]
print(food[2])

food[0] = "sausage"#mutable
food.append("Hotdog")
food.pop() #remove last one
food.insert(0,"cake")
for x in food:
    print(x)'''

#Tuples -> groups related data
'''students = ("Ram", 21, "male")

print(students.count("Ram"))
print(students.index("male"))
for x in students:
    print(x)'''

#set -> unordered, unindexed(print garda jun order ma pani aaunasakcha , fast than list
'''utensils = {"fork","spoon","knife"}
dishes = {"bowl","plate","cup"}

utensils.add("napkin")
dishes.update(utensils)
dinner_table = utensils.union(dishes)

for i in dishes:
    print(i)

print(dinner_table)'''

#dictionary -> use hashing so fast, unique key:value
'''capitals = {"USA": "Washington",
            "India": "ND",
            "Nepal": "Kathmandu"}
capitals.update({"India": "Mumbia"})
capitals.pop("USA")

print(capitals.get("Germany"))
print(capitals.keys())
print(capitals.items())

for key,value in capitals.items():
    print(key,value)'''

#index operator [] = gives access to sequence's element (str,lists,tup)

'''name = "ram Krishna"
if (name[0].islower()):
    name = name.capitalize()

first = name[:3].upper()
last = name[4:].lower()

print(name)
print(first)
print(last)'''



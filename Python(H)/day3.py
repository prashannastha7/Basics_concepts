# 17. Basis File IO
"""
"r" : r mode opens a file for read-only. We do not have permission to update or change any data in this mode.
"w" : w mode does not concern itself with what is present in the file. It just opens a file for writing and if there
is already some data present in the file, it overwrites it.
"x":x is used to create a new file. It does not work for an already existing file, as in such cases the operation fails.
"a" : a stands for append, which means to add something to the end of the file. It does exactly the same. It just
adds the data we like in write(w) mode but instead of overwriting it just adds it to the end of the file. It also
does not have the permission of reading the file.
"t" : t mode is used to open our file in text mode and only proper text files can be opened by it. It deals with the
file data as a string.
"b" : b stands for binary and this mode can only open the binary files, that are read in bytes. The binary files
include images, documents, or all other files that require specific software to be read.
"+" : In plus mode, we can read and write a file simultaneously. The mode is mostly used in cases where we want to
update our file. """

# 18. Reading
"""f = open("ps.txt", "r")
# f = open("ps.txt", "rb")
content = f.read()
print(content)

f.close()
f = open("ps.txt", "r")
content = f.read(3)
print(content)
content = f.read(4)
print(content)
#For loop
f = open("ps.txt", "r")
for line in f:
    print(line, end="")
f.close()

f = open("ps.txt", "r")
print(f.readline(), end="")
#print(f.readline())
f.close()"""

# 19. Write_and_append
"""f = open("ps1.txt", "w")
f.write("Hello I am Prashanna")
f.close()

f = open("ps1.txt", "a")
f.write("Hello I am Prashanna\n")
f.close()

f = open("ps.txt", "r+")
print(f.read())
f.write("\n Thnk you")
f.close()"""

# 20. Astrologer's Stars
"""a = int(input("please add number of line you want to print: "))
b = bool(int(input("please add 0 for False ")))

def star(a, b):
    if b == True:
        c = 1
        while c <= a:
            print(c * "*")
            c = c + 1
    else:
        while a > 0:
            print(a * "*")
            a = a - 1


star(a, b)"""

# 21. Seek(), tell()
"""f = open("ps.txt")
print(f.tell())  # tell where is the pointer character
print(f.readline())
print(f.tell())
print(f.readline())
# f.seek(0) # return pointer to the 0 character
print(f.tell())
print(f.readline())
f.close()"""


# 22. Health Management System
"""# 3 clients - Harry, Rohan and Hammad

def getdate():
    import datetime
    return datetime.datetime.now()


# write a function that when executed takes as input client name
# One more function to retrieve exercise or food for any client

import datetime

def gettime():
    return datetime.datetime.now()


def take(k):
    if k == 1:
        c = int(input("Enter 1 for exercise and 2 for food "))
        if (c == 1):
            value = input("Type here\n")
            with open("harry-ex.txt", "a") as op:
                op.write(str([str(gettime())]) + ": " + value + "\n")
            print("successfully written")
        elif (c == 2):
            value = input("Type here\n")
            with open("harry-food.txt", "a") as op:
                op.write(str([str(gettime())]) + ": " + value + "\n")
            print("successfully written")
    elif (k == 2):
        c = int(input("Enter 1 for exercise and 2 for food "))
        if (c == 1):
            value = input("Type here\n")
            with open("rohan-ex.txt", "a") as op:
                op.write(str([str(gettime())]) + ": " + value + "\n")
            print("successfully written")
        elif (c == 2):
            value = input("Type here\n")
            with open("rohan-food.txt", "a") as op:
                op.write(str([str(gettime())]) + ": " + value + "\n")
            print("successfully written")
    elif (k == 3):
        c = int(input("Enter 1 for exercise and 2 for food "))
        if (c == 1):
            value = input("Type here\n")
            with open("hammad-ex.txt", "a") as op:
                op.write(str([str(gettime())]) + ": " + value + "\n")
            print("successfully written")
        elif (c == 2):
            value = input("Type here\n")
            with open("hammad-food.txt", "a") as op:
                op.write(str([str(gettime())]) + ": " + value + "\n")
            print("successfully written")
    else:
        print("Please enter valid input (1(harry),2(rohan),3(hammad)")


def retrieve(k):
    if k == 1:
        c = int(input("Enter 1 for exercise and 2 for food "))
        if (c == 1):
            with open("harry-ex.txt") as op:
                for i in op:
                    print(i, end="")
        elif (c == 2):
            with open("harry-food.txt") as op:
                for i in op:
                    print(i, end="")
    elif k == 2:
        c = int(input("Enter 1 for exercise and 2 for food "))
        if (c == 1):
            with open("rohan-ex.txt") as op:
                for i in op:
                    print(i, end="")
        elif (c == 2):
            with open("rohan-food.txt") as op:
                for i in op:
                    print(i, end="")
    elif (k == 3):
        c = int(input("Enter 1 for exercise and 2 for food "))
        if (c == 1):
            with open("hammad-ex.txt") as op:
                for i in op:
                    print(i, end="")
        elif (c == 2):
            with open("hammad-food.txt") as op:
                for i in op:
                    print(i, end="")
    else:
        print("Please enter valid input (harry,rohan,hammad)")


print("------Health Management System------ ")
a = int(input("Press 1 for log the value and 2 for retrieve "))

if a == 1:
    b = int(input("Press 1 for harry 2 for rohan 3 for hammad "))
    take(b)
else:
    b = int(input("Press 1 for harry 2 for rohan 3 for hammad "))
    retrieve(b)
"""
# 23. Global variable
"""a = 10  # Global


def func(n):
    m = 8  # local
    global a  # used to change the value of global variable
    a = a + 45
    print(a, m)
    print(n, "I have printed")


func("This is me")


def harry():
    x = 20

    def rohan():
        global x  # it doesn't change becoz global le sidhai mathi hercha local ma hoina
        x = 88
    print("before calling ", x)
    rohan()
    print("after calling ", x)

harry()
print(x)  # global x gara pasi global variable banaucha so tei result aayo  
"""

#  Recursive Vs Iterative Approach
"""def factorial_iterative(n):
    fac = 1
    for i in range(n):  # 0 dekhi n-1 samma jancha
        fac = fac * (i+1)
    return fac

def factorial_recursive(n):
    if n == 1:
        return 1
    else:
       return n * factorial_recursive(n-1) # 5 * factorial_recursive(4)
                                        # 5 * 4 * factorial_recursive(3)


number = int(input("Enter your number: "))
print("Using iterative", factorial_iterative(number))
print("Using recursive", factorial_recursive(number))

# fibonacci 0 1 1 2 3 5 8 13
def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)

number = int(input("Enter your number: "))
print(fibonacci(number))"""

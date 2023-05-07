# scripting language( os module time module
"""import os


def current_directory():
    cwd = os.getcwd()  # cwd=current working directory
    print(cwd)


def file_path(filenames):
    path = os.path.abspath(filenames)
    print(path)


current_directory()
filename = "Library.py"
file_path(filename)

import time

sec = time.time()  # this print the sec that have pass from jan 1
print(sec)
localtime = time.localtime(sec)
print(localtime)
print(localtime.tm_year)

print(time.ctime(sec))

import smtplib  # simple mail transfer protocol

smtObj=smtplib.SMTP("smtp.gmail.com", 587)  # domain name and port number
smtObj.ehlo()   # used to tell server am present hello
smtObj.starttls()  # code number is from tls
smtObj.ehlo()
smtObj.login("prashannashrestha711@gmail.com", "email password")
smtObj.sendmail("prashannashrestha711@gmail.com", "prashannabdrshrestha711@gmail.com", "Subject:SMTP check")
smtObj.quit()"""

#*args -> more than one argument can be passed
"""def func1(*args):
    for i in args:
        print(i)


func1(10, 20, 30, "prashanna")

def funcargs(*args):
    print(args)
    print(type(args))

har = ["Prashanna", "Sus", "Gas"]
funcargs(har)
funcargs(*har)

def func1(**kwargs):
    for i in kwargs.items():
        print(i)


func1(a=10, b= 20, c= 30, d="prashanna")"""

# Factory -> Factory method is a creational design pattern which solves the problem of creating product objects
# without specifying their concrete classes. Factory Method defines a method,which should be used for creating
# objects instead of direct constructor call ( new operator).
"""def func1(called_func):
    print("This is the first function.")

    def nested_func1(called_func):
        print("This is the nested function.")
        called_func()
    return nested_func1(called_func)


def outer_func():
    print("This is the outer  function.")


func1(outer_func)"""

# NUMPY
"""import numpy as np

a = np.array([1, 2, 3]), ([2, 3, 5])
print(a)

import time
import sys

#compare of memory with numpy and array
b=range(1000)
print(sys.getsizeof(5)* len(b))

c = np.arange(1000)
print(c.size*c.itemsize)

#time consuming
size = 100000
L1 = range(size)
L2 = range(size)
A1 = np.arange(size)
A2 = np.arange(size)

start = time.time()
result = [(x+y) for x,y in zip(L1, L2)]
print(result)
print("Python list took ", (time.time() - start)*1000)

start = time.time()
result = A1 + A2
print("Numpy array took ", (time.time() - start)*1000)

a = np.array([1, 2]),([3, 4]), ([5, 6])
b = np.array([[1, 2],[3, 4], [5, 6]])
print(a)
print(b)

print(b.ndim)
print(b.itemsize)
print(b.shape)  # most used
b = np.array([[1, 2],[3, 4], [5, 6]], dtype=np.float64)
print(b)
print(b.itemsize)
print(b.shape)
b = np.array([[1, 2], [3, 4], [5, 6]], dtype=np.complex128)  # 64 bits ->128
print(b)

print(np.zeros((3, 4)))
print(np.ones((3, 4)))

print(range(5))
print(np.arange(5))
print("Concatenation example: ")
print(np.char.add(["hello", "hi"], ["abc", "pras"]))
print(np.char.multiply("hello \n", 5))
print(np.char.center("hello", 20, fillchar="-"))
print(np.char.capitalize("hello people"))
print(np.char.title("hello people"))
print(np.char.lower(["KEM CHO"]))
print(np.char.lower("KEM CHO"))
print(np.char.split("kem cho? majama?"))
print(np.char.splitlines("kem cho?\n majama?"))
print(np.char.join([':', '-'], ['dmy', 'ymd']))
print(np.char.replace("Hello Gujrati", "Hello", "kem cho?"))"""

# Pandas
"""import pandas as pd
#print(pd.__version__)

# SERIES create, manipulate, querry, delete

# creating a series form a list
arr = [0, 1, 2, 3]
s1 = pd.Series(arr)
print(s1)

order = [1, 2, 3, 4]
print(pd.Series(arr, index=order))

import numpy as np

n = np.random.rand(5)  # create a random Ndarray
index = ['a', 'b', 'c', 'd', 'e']
print(pd.Series(n, index=index))

#create series form dictionary
d={'a': 1, 'b': 2, 'c': 3}
s3 = pd.Series(d)
print(s3)

# modify the index of series
print(s1)
s1.index = ['A', 'B', 'C', 'D']
print(s1)

#slicing
print(s1[:3])

#append
s4 = s1.append(s3)
print(s4)
print(s4.drop('b'))

arr1 = [0, 1, 2, 3, 4, 5]
arr2 = [6, 7, 8, 9, 5]
s5 = pd.Series(arr1)
s6 = pd.Series(arr2)

print(s5)
print(s6)

print(s5.add(s6))  #sub mul div s5.median() s5.max()

# Create Dataframe
import numpy as np
dates = pd.date_range('today', periods=6) #Define time sequence as index
num_arr = np.random.randn(6, 4)
columns = ['A', 'B', 'C', 'D']

df1 = pd.DataFrame(num_arr, index=dates, columns=columns)
print(df1)
# create with dic array
data = {'animal': ['cat', 'cat', 'snake', 'dog', 'dog', 'cat', 'snake', 'cat', 'dog', 'dog'],
        'age' : [2.5,3,0.5,np.nan, 5, 2, 4.5, np.nan, 7, 3],
        'visits' : [1, 3, 2, 3, 2, 3, 1, 1, 2, 1]}
labels = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']

df2 = (pd.DataFrame(data, index=labels))
print(df2)
print(df2.dtypes)
print(df2.head(5))  # tail(2)

#see statistical data of dataframe
print(df2.describe())
print(df2.T)
print(df2.sort_values(by='age'))

# slicing by tag
print(df2[['age','visits']])
df3 = df2.copy()
print(df3)
print(df3.mean())
print['visits'].sum

# File operation
df3.to_excel('animal.xlsx', sheet_name ='Sheet1')
df_animal2 = pd.read_excel('animal.xlsx' , 'Sheet1', index_col=None, na_values=['NA'])
print(df_animal2)"""
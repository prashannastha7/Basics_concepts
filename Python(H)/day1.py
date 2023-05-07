# 1.Variable and Datatype
"""var1 = "Hello World"
var2 = 4
var3 = 50.5
var4 = "30"
var5 = "20"
print(var1 + var4)
print(type(var2))
print(int(var4) + int(var5)) # typecasting
print(10 * "Hello World \n", end="") """

#input garda string huncha data types
#2. user_input
"""print("Enter your number")
number= int(input())
print("You entered ", number+10)
"""
# Quiz1
"""print("Enter your  two number")
num1 = int(input())
num2 = int(input())
print("Your sum is = ", num1+num2)"""

#3. String_Slicing
"""stg = 'Tim said, "I\'m busy today" '
print(stg)

na = "Prashanna Bdr Shrestha"
print(len(na))
print(na[2:9]) # aagadi ko chodney(2-> r) pasadi ko chai include huncha
print(na[-2])
print(na[0:9:2]) #skip 1
print(na[0:])
print(na[::-1]) #to reverse

#String_Function
print(na.endswith("Shrestha")) #condition check garney
print(na.isalnum())
print(na.count("a"))
print(na.find("Bdr"))
print(na.upper())
print(na.replace("Bdr", "Bahadur"))
print(na.split(" "))
"""
#4. List is written inside []
"""grocery = ["Hairpin", "Chocolates", "Vegetables", "Meat", "Fresher", "69"]
print(grocery[0:2])
#list_function
numbers = [1, 5, 3, 14]
#numbers.sort()
print(max(numbers))
numbers.remove(5)
numbers.append(7)
numbers.insert(2, 100)
numbers.sort(reverse=True)
print(numbers)
num = []
num.append(7)
num.append(76)
num.append(69)
num.sort()
print(num)
num[0] = 80
print(num)
numb = [1, 2, 3, 4]
one, *other = numb # * means list
print(one)
print(other)
l = [1, 2, 3]
tup = tuple(l)
print(tup)"""

#5. tuple is written in () and is immutable
"""tp = (1)
tp1 = (1,) # is_tuple put , for only one element
print(tp)
print(tp1)
a = 1
b = 8
a, b = b, a
# temp = a
# a = b
# b = a
print(a, b)
list=[(1, 2, 3),(4, 5, 6)]
print(list)
list.append(("Tuple","inside"))
print(list)"""

#Nesting lists within tuples
"""tpl = (['a', 'b', 'c'],['d', 'e'])
print(tpl)
tpl[0].append('z')
print(tpl)"""

#6. Dictionary is written in {},  combination of keys and value and unordered unlike tup and lis
"""d1 = {}
#print(type(d1))
d2 = {" Maths": "Rs.400", "DL": "Rs.600", "OOP": "Rs.350", "Discrete": {"N":"Rs.400", "F":"Rs.800"}}
#Mutable
d2["Physics"] = "Rs.500"
print(d2)
print(d2["Discrete"])
print(d2["Discrete"]["F"])
del d2["DL"]
print(d2)
# key can be int as well
dict={1: "Welcome", 2: "to", 3: "house"}
print(dict)
# Dic_Function
d3 = d2.copy()
del d3[" Maths"]
print(d3)
print(d2)
print(d2.get(" Maths"))
print(d2.keys())
d5= dict([(1,"Welcome"),(2,"to"),(3,"house")])
print(d5)
"""
#7. Create dictionary
"""dict = {"proficient": "competent or skilled in doing or using something.", "random":
"made, done, or happening without method or conscious decision.", "append": "add to the end of a written document."}

print("proficient, random, append")
print("Enter those words to know their meaning")
words = input()
print(dict[words])"""

#8. Sets
"""s = set()
lists = {1, 2, 3, 4}
print(lists)
print(type(lists))
s.add(1)
s.add(1)
print(s)  # sets put another unique value unlike lists
s.add(1)
s.add(2)
s1 = s.union({1, 2, 3})
s2 = s.intersection()
s3 = {4, 6}
print(s, s2)
print(s.isdisjoint(s3))
#frozenset is immutable 
fs=frozenset([1,2,3,4])
fs.add('a')
print(fs)
"""

#9. IF_ELSE
"""no = [1, 2, 3, 5]
print(5 in no)
if 5 in no:
    print("Yes it is in no")"""

# Quiz2
"""print("Please enter you age: ")
age = int(input())
if age < 7 or age > 100:
    print("Invalid")

elif age > 18:
    print("You can have license")
elif age == 18:
    print("Come back after 1 year")
else:
    print("You cannot have license yet")"""

#10. Faulty_Calc
"""print("Enter 1st Number")
num1 = int(input())
print('Enter 2nd Number')
num2 = int(input())
print('so What you Want?' + '+,-,/,%,*')
num3 = input()

if num1 == 45 and num2 == 3 and num3 == '*':
    print("555")
elif num1 == 56 and num2 == 9 and num3 == '+':
    print("77")
elif num1 == 56 and num2 == 6 and num3 == '/':
    print("4")
elif num3 == '*':
    num4 = num1 * num2
    print(num4)
elif num3 == '+':
    plus = num2 + num1
    print(plus)
elif num3 == '/':
    Dev = num2 / num1
    print(Dev)
elif num3 == '-':
    Dev = num2 - num1
    print(Dev)
elif num3 == '%':
    percent = num2 % num1
    print(percent)
else:
    print("Error! Please check your input")"""


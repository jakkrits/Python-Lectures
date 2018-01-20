greeting = "hey there"
print(greeting)
greeting = "changed from hey there to yo dude!"
print(greeting)

print(type(greeting))

""" 
String
"""
print(greeting.replace('e', 'E'))
print(greeting[0])
print(greeting[-1])
print(greeting[0:2]) # it doesnt include upperbound index
print(greeting[:2])
print("  " + greeting[2:])
print(greeting[-5:])

# greeting = input("Say your name \n")
# print("Hey " + greeting)

"""
List
"""
myList = ["Change", "my", "shit", 2, 90.02]
print(myList)
print(myList[0])
print(myList[2:])
print(type(myList))
print(type(myList[4]))
print(type(myList[-1]))
myList.append("added")
print(myList)
myList.remove("shit")
print(myList)

"""
Tuple --> IMMUTABLE
"""
myTuple = (2, 40, 209.92, "change")
print(myTuple)
print(myTuple[0:3])
print(myTuple[-3:-1])

"""
Dictionary
"""
myDict = {"Name": "Jakkrit", "LastName": "Sutt", "Age": 39, "HomeTuple": ("Korat", "Nice", "CPN"), "HomeList": [683, 8, "Keelaklang"]}
print(myDict["Name"])
print(myDict["HomeTuple"][2])
print(myDict["HomeList"][2])

"""
Casting
"""
myNumber = 10
print(myNumber)

print(float(myNumber))

"""
Function
"""
def currency_convert(rate, euros):
    dollars = euros * rate
    # print("Rate = , Amount = %d => %d", rate, euros, dollars)
    print('rate = {0}, amount = {1}, dollars = {2}'.format(rate, euros, dollars))
    return dollars

currency_convert(10, 99290)

"""
VISUAL PYTHON
"""
# Numbers are IMMUTABLE -> Reassigning value, it reserves the old where the new is occupying new memory spot.
# When old value is not used, it will fade away due to 'garbage collection' process.

# Testing if a and b are pointing to the same location.
a = 10
b = 10
print(id(a))
print(id(b))
print(a is b)
a = 11
b = 12
print(id(a))
print(id(b))
print(a is b)
a = b
print(id(a))
print(id(b))
print(a is b)

# PICTURE # ![1](assets/1-python-var-memory-address.png)

# Assigning multiple variables.
a = b = c = d = e = f = "multiple vars"
print(a, b, c, d, e, e is f)

# Naming convention = 1. starts with letter or underscore 2. contains only letters or numbers.

# Immutable Data 
# PICTURE 2

# Data Type
# PICTURE 3

# Multiline Text
long_text = ''' this is a long ass Text 
with multi line stuff
so damn long.'''
print(long_text)

# Casting string to number and back.
a = 10.5
b = "10.5"
c = str(a)
d = float(b)
print('c is {value_c}, and d is {value_d}'.format(value_c = c, value_d = d))

# Basic Math
# PICTURE 4 #

a = abs(-6)
print(a)

# Operation Precedence
# PICTURE 5 #

# String Operations
# PICTURE 6 #

name = "jakkrit suttanuruk"
print(name[0:5])
print(name[-5:])

print(len(name))

isAInThere = "a" in name 
print(isAInThere)

isANotInThere = "a" not in name
print(isANotInThere)

# String Concat
print(str(a) + b + "yes")

'''
FUNCTION
'''

def hi(nickname, name = "default name"): # Default argument follows non-default
    print("What up! " + name + " " + nickname)

hi(" Jakkrit", "Dave")
hi(nickname = "Davez")

def get_distance(speed, duration):
    distance_in_kilometer = speed * duration
    distance_in_meter = distance_in_kilometer * 1000
    return distance_in_meter

print(get_distance(90, 10))

'''
CONDITION
'''

def drive(car_speed):
    if car_speed > 100:
        print("too fast!!!")
    elif car_speed < 0:
        print("too slow")
    else:
        print("OK!")

drive(1200)
drive(29)
drive(-20)

'''
Boolean Expression
'''
print(1 == 2)
print("abc" != 2.5)
print(2.5 != 2.50)
x = True
y = False
z = None
print(id(a))
print(id(b))
print(x and y)
print(y or not x)
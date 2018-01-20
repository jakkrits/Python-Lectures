try:
    1/0
except ZeroDivisionError as e:
    print(str(e) + ". But it's ok")

'''
Custom Exception
'''

class HasWordFuck(Exception):
    pass

try:
    raise HasWordFuck("It contains 'FUCK' ")
except HasWordFuck as e:
    print("This is not acceptable. " + str(e))
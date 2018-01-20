'''
Lists, Tuples, Dictionaries
'''

# PICTURE 7 #

# Lists and Dictionaries are MUTABLE
# Tuples are IMMUTABLE
my_tuple = (1, "cat", 2.30)
print(my_tuple[1:])
print(my_tuple[1][0:2])
print(type(my_tuple))
print(len(my_tuple))

# my_tuple[0] = "2" --> Error

my_list = [1, "cat", 2.30]
my_list[1] = "cat and dog"
print(my_list)
print(my_list[1][-5:])
# my_list[1][0] = "C" --> ERROR (String is IMMUTABLE)
# print(my_list) 

new_list = my_list.append([1, 'sk', ('ks', 1, 3)])
print(new_list) # return None (lists are MUTABLE)
print(my_list) # appends to the same location

my_list.pop()
print(my_list)

my_list.insert(len(my_list) -1, "INSERTED VALUE")
print(my_list)


#########
# Dictionary
#########

ages = {
    'สมสัก': 39,
    'somsak': 58,
    'SJ': 31,
    'Sandra': 29
}
print(ages)
somsak_age = ages['สมสัก']
print(somsak_age)
ages['SJ'] = 82 - 83
print(ages)
ages.pop('สมสัก')
print(ages)
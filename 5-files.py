the_file = open("integers.txt", "w")

integers = [1, 2, 3, 4, 5]
for integer in integers:
    the_file.write(str(integer) + '\n')

the_file.close()

the_file = open("integers.txt")
# print(the_file.readlines())

lines = the_file.readlines()
for line in lines:
    print('this is line: ', line)
the_file.close()
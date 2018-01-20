laps = 0
while laps < 10:
    laps += 1
    print(laps)
    print("and")
    if(laps % 2) == 0:
        print("EVEN")
        continue
    if(laps == 9):
        break
else:
    print("laps > 10")
print("\tdone\n\n")

my_loop = ["one", "two", "three", 4, "five", "six", 7, 8]
for item in my_loop:
    print('\t{0}'.format(item))
    print(type(item))
    if type(item) != type("string"):
        break

for _ in my_loop:
    print(my_loop)

for item in my_loop:
    if type(item) != type(0):
        continue
    print(item)

phone_numbers = {
    "dave": "920-292-3992",
    "ping": "292-329-3492",
    "fon": "294-931-4847"
}

for name in phone_numbers:
    print('the number of {0} is {1}'.format(name, phone_numbers[name]))


lorem_text = '''
lorem ipsum ksor jakrit 
lsk oki sis ido thai aidk 
knsn dora a the best doraemon 
al modn lsk why is dora doraemon is 
the best?
'''

# find "dora bla bla bla doraemon"
import re
found = re.search("dora.*doraemon", lorem_text)
print(found)
print(type(found)) # -> type Matach

not_found = re.search("jakkrit", lorem_text)
print(not_found)
print(type(not_found))

print(found.start())
print(found.end())

print(found.group())
print(lorem_text[56:80])
# If multiple occurences are found, only returns the first one.

# go through all occurences use, re.finditer
print(list(re.finditer("dora.*doraemon", lorem_text)))

# check if string matches pattern use, re.match
print(bool(re.match("[0-9][a-z]", "9z0")))
print(bool(re.match("[0-9][a-z][0-6]", "9z0")))

# substitute
new_text = re.sub("dora.*doraemon", "SUBBED", lorem_text)
print(new_text)
print(lorem_text)
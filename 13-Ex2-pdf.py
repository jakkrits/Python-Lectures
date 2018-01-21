import slate
file = open('/assets/sample.pdf')
doc = slate.PDF(file)
print(doc)
print(doc[1])
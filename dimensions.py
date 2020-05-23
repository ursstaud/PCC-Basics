dimensions=(200,50)
print(dimensions[0])
print(dimensions[1])

tupleexample = (3,)
print(type(tupleexample))
anotherexample = (3)
print(type(anotherexample))

for dim in dimensions:
	print(dim)

print(f'\nThe original dimensions are:')
for dim in dimensions:
	print(dim)

dimensions=(400,100)
print(f'\nThe new dimensions are:')
for dim in dimensions:
	print(dim)
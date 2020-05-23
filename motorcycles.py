motorcycles = (['honda','yamaha','suzuki'])
print(motorcycles)
#motorcycles[0] = 'ducati'
#print(motorcycles)
motorcycles.append('ducati') #appending using a method that actually has something in the parenthesis
print(motorcycles)

othercycles = []
print(othercycles)

othercycles.append('ducati')
othercycles.append('honda')
othercycles.append('yamaha')
print(othercycles)

print(motorcycles)
motorcycles.insert(4, 'this is an example')
print(motorcycles)
motorcycles.insert(2, 'another one lool')
print(motorcycles)
del motorcycles[2]
print(motorcycles)
del motorcycles[4]
print(motorcycles)
print("i'm doing a great job :)")


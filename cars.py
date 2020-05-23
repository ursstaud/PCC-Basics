cars = ['bmw','audi','toyota','subaru']
cars.sort()
print(cars)
cars.sort(reverse=True)
print(cars)

print(f'\nHere is the original list: {cars}')
print(f'\nHere is the sorted list:')
print(sorted(cars))

print('\nHere is the original list again:')
print(cars)

print('\nHere is the list temporarily sorted in reverse:\n\n')
print(sorted(cars,reverse=True))

cars = ['bmw','audi','toyota','subaru']
print(cars)
cars.reverse()
print(cars)

print(len(cars))

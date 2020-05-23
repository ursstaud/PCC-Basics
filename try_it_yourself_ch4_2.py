for value in range(1,21):
	print(value)

big_numbers = list(range(1,1000001))
#for number in big_numbers:
#	print(number)

print(sum(big_numbers))
print(min(big_numbers))
print(max(big_numbers))

odd_numbers = list(range(1,21,2))
print(odd_numbers)

#numbers = [value*3 for value in range(1,31)]
#print(numbers)
numbers=[]
for number in range(1,31):
	threes=number*3
	numbers.append(threes*3)
print(numbers)

cubes = []
for number in range(0,11):
	cube = number**3
	cubes.append(cube)

cubes = [cube**3 for cube in range(0,11)]
print(cubes)
print(cubes)
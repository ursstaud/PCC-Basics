for value in range(6):
	print(value)

numbers = list(range(6))
print(numbers)

even_numbers = list(range(0,11,2))
print(even_numbers)

squares = []
for value in range(0,11):
	square = value**2 #the current value is raised to the second power and assigned to square
	squares.append(square) #appending the temporary variable value square to the squares
print(squares)

squares2 = []
for value in range(0,11):
	squares2.append(value**2)
print(squares2)

#list comprehension
example = [value**2 for value in range(0,11)]
print(example)
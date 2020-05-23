print("Please add two numbers:")
while True:
	first_number = input("First number: ")
	second_number = input("Second number: ")
	try:
		answer = int(first_number) + int(second_number)
	except ValueError:
		print("You cannot add non-numeric values.")
	else:
		print(answer)
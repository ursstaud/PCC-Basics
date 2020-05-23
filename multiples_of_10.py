number = input("Please provide a number and I will tell you if it is divisible by 10: ")
number = int(number)

if number % 10 == 0:
	print(f"{number} is divisible by 10.")
else:
	print(f"{number} is not divisible by 10.")
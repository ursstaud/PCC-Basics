filename = 'poll.txt'

print("Hello, please answer the following question:")

while True:
	response = input("What is your favorite thing about programming? ")
	with open(filename, 'a') as pollfile:
		pollfile.write(f"{response}\n")
	print("Thank you for your answer.")
	again = input("Would you like to add another reason? y/n ")
	if again == 'n':
		break
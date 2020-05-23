filename = 'guestbook.txt'

while True:
	name = input("Hello, please enter your name so I can add you to the guest book. Type quit at any time to exit. ")
	if name == 'quit':
		break
	with open(filename, 'a') as file_object:
		file_object.write(f"{name.title()}\n")
	print(f"Thank you for adding your name to the guestbook, {name.title()}.")
	response = input("Would you like to add another name to the guestbook? y/n ")
	if response == 'n':
		print("Thank you for using our service. Goodbye!")
		break
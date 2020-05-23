responses = {}

polling_active = True

while polling_active:
	name = input("\nWhat is your name? ")
	response = input("\nIf you could visit one place in the world, where would you go? ")

	#storing the responses in a dictionary
	responses[name] = response

	repeat = input("Would anyone else like to take the poll? (yes or no) ")
	if repeat == 'no':
		polling_active = False

#polling complete
print("---Polling Results---")
for name, result in responses.items():
	print(f"{name.title()} would like to visit {result.title()}!")
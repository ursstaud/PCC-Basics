responses={}

#setting a flag to show that polling is active
polling_active = True

while polling_active:
	#prompt for person's name and response
	name = input("\nWhat is your name? ")
	response = input("\nWhich mountain would you like to climb someday? ")
	#store the responses in a dictionary
	responses[name] = response
	#find out if anyone else is going to take the poll
	repeat = input("Would you like to let another person respond? (yes/no) ")
	if repeat == "no":
		polling_active = False

#polling is complete. show results
print("\n-----Poll Results-----")
for name, response in responses.items():
	print(f"{name.title()} would like to climb {response.title()}!")
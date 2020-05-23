#movie tickets 
#prompt = "What is your age so I can determine the correct ticket price? Please type 'quit' to end. "


#active = True

#while active == True:
#	age = input(prompt) #this value needs to be inside the while loop to prevent an infinite loop
#	if age == 'quit':
#		break
#	age = int(age)
#	if age < 3:
#		print("Your ticket is free!")
#	elif age >= 3 and  age < 12:
#		print("Your ticket will be 10 dollars!")
#	else:
#		print("Your ticket will be 15 dollars!")


#round 2 rewrite
prompt = "What is your age so I can determine the correct ticket price? Please type 'quit' to end. "
age = ""

while age != 'quit':
	age = input(prompt)
	if age != 'quit':
		age = int(age)
		if age < 3:
			print("Your ticket is free!")
		elif age >= 3 and  age < 12:
			print("Your ticket will be 10 dollars!")
		else:
			print("Your ticket will be 15 dollars!")
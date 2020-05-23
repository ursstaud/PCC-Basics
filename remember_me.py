import json

#load the username if it has been stored previously
#otherwise, prompt for the username and store it

filename = 'username.json'

try:
	with open(filename) as file:
		username = json.load(file)
except FileNotFoundError:
	username = input("What is your name? ")
	with open(filename, 'w') as file:
		json.dump(username, file)
		print(f"We will remember you when you come back {username}!")

else:
	print(f"Welcome back, {username}!")
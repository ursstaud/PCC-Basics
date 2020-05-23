import json

def get_stored_username():
	"""get stored username if available"""
	filename = 'username.json'
	try:
		with open(filename) as file:
			username = json.load(file)
	except FileNotFoundError:
		return None 
	else:
		return username

def get_new_username():
	"""prompt for a new username"""
	username = input("What is your name? ")
	filename = 'username.json'
	with open(filename, 'w') as file:
		json.dump(username, file)
	return username

def greet_user():
	"""Greet the user by name"""
	username = get_stored_username()
	response = input(f"Is {username} the correct username you would like to login with? y/n ")
	if response == 'y':
		print(f"Welcome back, {username}!")
	else:
		username = get_new_username()
		print(f"We'll remembery you when you come back, {username}!")

greet_user()
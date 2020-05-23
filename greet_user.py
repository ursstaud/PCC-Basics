import json

filename = 'username.json'

with open(filename) as file:
	username = json.load(file)
	print(f"Welcome back, {username}!")
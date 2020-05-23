import json

def get_favorite_number():
	favorite_number = input("What is your favorite number? ")
	filename = 'favoritenumber.json'
	with open(filename, 'w') as file:
		json.dump(favorite_number, file)
	return favorite_number
	
def load_favorite_number():
	filename = 'favoritenumber.json'
	try:
		with open(filename) as file:
			favorite_number = json.load(file) 
	except FileNotFoundError:
		return None
	else:
		return favorite_number

def favorite_number():
	"""checks and displays favorite number, asks for fav number if dne"""
	favorite_number = load_favorite_number()
	if favorite_number:
		print(f"I know your favorite number, it is {favorite_number}!")
	else:
		favorite_number = get_favorite_number()
		print(f"I'll remember your favorite number of {favorite_number} when you come back.")

favorite_number()





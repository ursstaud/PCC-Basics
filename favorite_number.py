import json

def store_favorite_number(favorite_number):
	filename = 'favoritenumber.json'
	with open(filename, 'w') as file:
		json.dump(favorite_number, file)
	
def load_favorite_number():
	filename = 'favoritenumber.json'
	with open(filename) as file:
		favorite_number = json.load(file) 
		return favorite_number

def favorite_number():
	favorite_number = input("What is your favorite number? ")
	store_favorite_number(favorite_number)
	favorite_number = load_favorite_number()
	print(f"I know your favorite number, it is {favorite_number}.")

favorite_number()





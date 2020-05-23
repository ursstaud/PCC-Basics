def describe_pets(animal_type,animal_name):
	"""displays information about a pet"""
	print(f"\nI have a {animal_type}.")
	print(f"My {animal_type}'s name is {animal_name.title()}.")

describe_pets('hamster','harry')
describe_pets('dog','doug')

describe_pets('Pat', 'cat')

describe_pets(animal_type='hamster',animal_name='harry')
describe_pets(animal_name = 'noodles',animal_type='pupper')
def describe_pet(pet_name, animal_type = 'dog'):
	print(f"\nI have a {animal_type}.")
	print(f"\nMy {animal_type}'s name is {pet_name.title()}.")

#a dog named willie
describe_pet('willie')
describe_pet(pet_name = 'willie')

#a hamster named harry
describe_pet('harry', 'hamster')
describe_pet(animal_type='hamster', pet_name='harry')
describe_pet(pet_name='harry', animal_type='hamster')

describe_pet()
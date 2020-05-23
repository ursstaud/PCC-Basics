def describe_pet(pet_name, pet_type = 'dog'):
	"""describing animals"""
	print(f"I have a {pet_type}.")
	print(f"My {pet_type}'s name is {pet_name.title()}.")

describe_pet(pet_name='squisher')
describe_pet('noodles')
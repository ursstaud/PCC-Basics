def make_pizza(size, *toppings):
	"""summarize the pizza that's going to be made"""
	print(f"\nMaking a {size}-inch pizza with the following toppings:")
	for topping in toppings:
		print(f"-{topping}")

make_pizza(12, 'pepperoni')
make_pizza(16, 'garlic','black olives','cashews')
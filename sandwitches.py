def make_sandwitch(bread, meat, cheese, *topping):
	"""printing sandwitch order"""
	print(f"You have ordered a(n) {meat} and {cheese} sandwitch on {bread} bread with the following toppings:")
	for toppings in topping:
		print(f"{toppings}")

make_sandwitch('gluten free','turkey','no cheese','oil','pepperoncini','avocado')
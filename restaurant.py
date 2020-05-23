class Restaurant:
	"""describing a restaurant"""

	def __init__(self, restaurant_name, cuisine_type):
		self.restaurant_name = restaurant_name
		self.cuisine_type = cuisine_type

	def describe_restaurant(self):
		"""describes restaurant"""
		print(f"The restaurant {self.restaurant_name.title()} serves {self.cuisine_type.title()} food.")

	def open_restaurant(self):
		"""tells you if the restaurant is open"""
		print(f"The restaurant {self.restaurant_name.title()} is now open.")

kickin_chicken = Restaurant('kickin chicken', 'american/asian fusion')

print(f"My favorite place to eat is at {kickin_chicken.restaurant_name.title()}.")
print(f"{kickin_chicken.restaurant_name.title()} serves {kickin_chicken.cuisine_type.title()} food.\n")

taqueria_los_pericos = Restaurant('taqueria los pericos', 'mexican')
print(f"I also really like to eat at {taqueria_los_pericos.restaurant_name.title()}.")
print(f"{taqueria_los_pericos.restaurant_name.title()} serves {taqueria_los_pericos.cuisine_type.title()} food.")

kickin_chicken.describe_restaurant()
taqueria_los_pericos.describe_restaurant()

kickin_chicken.open_restaurant()
taqueria_los_pericos.open_restaurant()

restaurante_italiano = Restaurant('restaurante italiano', 'italian')
real_thai = Restaurant('real thai kitchen', 'thai')
shogun = Restaurant('shogun sushi', 'japanese')

restaurante_italiano.describe_restaurant()
real_thai.describe_restaurant()
shogun.describe_restaurant()
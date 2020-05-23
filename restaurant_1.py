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
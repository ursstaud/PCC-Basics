class Restaurant:
	"""describing a restaurant"""

	def __init__(self, restaurant_name, cuisine_type):
		self.restaurant_name = restaurant_name
		self.cuisine_type = cuisine_type
		self.number_served = 0

	def describe_restaurant(self):
		"""describes restaurant"""
		print(f"The restaurant {self.restaurant_name.title()} serves {self.cuisine_type.title()} food.")

	def open_restaurant(self):
		"""tells you if the restaurant is open"""
		print(f"The restaurant {self.restaurant_name.title()} is now open.")

	def set_numbers_served(self): #only need to specify another parameter if you're doing some manipulation to the variable
	#if you're just printing, leave it as self
		print(f"{self.restaurant_name} has served {self.number_served} people.")

	def increment_number_served(self, already_served):
		"""increments the number of customers who have already been served"""
		self.number_served += already_served
		print(f"The restaurant has served {self.number_served} people now.")

restaurant = Restaurant('restaurant', 'american')
#print(f"{restaurant.restaurant_name.title()} has served {restaurant.number_served} people")

restaurant.number_served = 500

restaurant.set_numbers_served()

restaurant.increment_number_served(20)
restaurant.increment_number_served(200)
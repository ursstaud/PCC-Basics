from restaurant import Restaurant


class IceCreamStand(Restaurant):
	"""basic example of parent child classes"""
	def __init__(self, restaurant_name, cuisine_type):
		super().__init__(restaurant_name,cuisine_type)
		self.flavors = ['chocolate', 'vanilla','strawberry']

	def flavors_in_stock(self):
		print(f"Today at {self.restaurant_name.title()}, we currently have the following flavors in stock:")
		for flavor in self.flavors:
			print(flavor)

marianne=IceCreamStand('Mariannes', 'Ice Cream')

marianne.flavors_in_stock()

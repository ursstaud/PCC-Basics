class Car:
	"""a simple attempt to represent a car"""

	def __init__(self, make, model, year):
		"""initialize attributes to describe a car"""
		self.make = make
		self.model = model
		self.year = year
		self.odometer_reading = 0

	def get_descriptive_name(self):
		"""return a neatly formatted descriptive name"""
		long_name = f"{self.year} {self.make} {self.model}" #we are adding self.xyz because it references that specific instance i created
		return long_name.title()

	def read_odometer(self):
		"""return odometer reading thing"""
		print(f"This car has {self.odometer_reading} miles on it.")

my_new_car = Car('audi', 'a4', 2019)
print(my_new_car.get_descriptive_name())

my_new_car.read_odometer()

my_new_car.odometer_reading = 23
my_new_car.read_odometer()

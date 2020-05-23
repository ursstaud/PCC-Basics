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

	def update_odometer(self, mileage): #created a mileage value that is replaced with odometer reading
		"""set the odometer reading to the given value
		reject the change if it attempts to roll the odometer back"""
		if mileage >= self.odometer_reading:
			self.odometer_reading = mileage
			print(f"This car now has {self.odometer_reading} miles on it.")
		else:
			print("You can't roll back an odometer!")

	def increment_odometer(self, miles):
		"""add the given amount to the odometer reading"""
		self.odometer_reading += miles

	def read_odometer(self):
		"""return odometer reading thing"""
		print(f"This car has {self.odometer_reading} miles on it.")

	def gas_tank(self):
		print(f"This car has a gas tank.")


class ElectricCar(Car):
	"""represent aspects of a car, specific to electric vehicles"""
	def __init__(self, make, model, year):
		"""initialize attributes of the parent class"""
		super().__init__(make, model, year)
		self.battery_size = 90

	def describe_battery(self):
		print(f"This car has a {self.battery_size}-kWh battery.")

	def gas_tank(self):
		print(f"This car is electric, so it does not have a gas tank.")

my_tesla = ElectricCar('tesla', 'cyber truck', '2020')

print(my_tesla.get_descriptive_name())

my_tesla.describe_battery()

my_scion = Car('scion', 'tc', '2006')

my_scion.gas_tank()

my_tesla.gas_tank()
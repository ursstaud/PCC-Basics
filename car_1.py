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


class Battery:
	"""a simple attempt to model ab attery for an electric car"""
	def __init__(self, battery_size=75):
		self.battery_size = battery_size

	def describe_battery(self):
		"""printing statement"""
		print(f"This car has a {self.battery_size}-kWh battery.")

	def get_range(self):
		"""print info about the range this battery provides"""
		if self.battery_size == 75:
			range = 260
		elif self.battery_size == 100:
			range = 315
		print(f"This car can go about {range} miles on a full charge.")

	def upgrade_battery(self):
		if self.battery_size < 100:
			self.battery_size = 100


class ElectricCar(Car):
	"""represent aspects of a car, specific to electric vehicles"""
	def __init__(self, make, model, year):
		"""initialize attributes of the parent class"""
		super().__init__(make, model, year)
		self.battery = Battery()

	def gas_tank(self):
		print(f"This car is electric, so it does not have a gas tank.")
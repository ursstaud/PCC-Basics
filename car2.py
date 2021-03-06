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

my_new_car = Car('audi', 'a4', 2019)
print(my_new_car.get_descriptive_name())

my_new_car.update_odometer(23) #doesn't spit out text, only changes value
my_new_car.update_odometer(12)

my_new_car.increment_odometer(23_500)
my_new_car.read_odometer()
my_new_car.increment_odometer(100)
my_new_car.read_odometer()
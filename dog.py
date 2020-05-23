class Dog: 
	"""a simple attempt to model a dog."""

	def __init__(self, name, age):
		"""initialize name and age attributes"""
		self.name = name
		self.age = age

	def sit(self):
		"""simulate a dog sitting in response to a command"""
		print(f"{self.name} is now sitting.")

	def roll_over(self):
		"""simulate a dog rolling over in response to a command"""
		print(f"{self.name} is now rolled over.")

my_dog = Dog("Glob", 10)
your_dog = Dog("Rex", 3)

print(f"My dog's name is {my_dog.name.title()}.")
print(f"{my_dog.name.title()} is {my_dog.age} years old.")

my_dog.sit()
my_dog.roll_over()

print(f"\nYour dog's name is {your_dog.name.title()}.")
print(f"{your_dog.name.title()} is {your_dog.age} years old.")

your_dog.sit()
your_dog.roll_over()
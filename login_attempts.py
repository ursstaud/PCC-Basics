class Users:
	"""simple class example with users"""
	def __init__(self, first_name, last_name, age, location):
		self.first_name = first_name
		self.last_name = last_name
		self.age = age
		self.location = location
		self.login_attempts = 0

	def describe_user(self):
		"""describing the user example"""
		print(f"This user's full name is {self.first_name.title()} {self.last_name.title()}.")
		print(f"This user's age is {self.age}, and their location is in {self.location.title()}.")

	def greet_user(self):
		full_name = f"{self.first_name.title()} {self.last_name.title()}"
		print(f"Hello {full_name}, welcome!")

	def login_attempt(self):
		self.login_attempts = self.login_attempts + 1
		return self.login_attempts

	def reset_attempts(self):
		self.login_attempts = self.login_attempts * 0
		return self.login_attempts

	def increment_login_attempts(self, login_number):
		self.login_attempts += login_number
		print(f"The user has logged in {self.login_attempts} times now.")


user1 = Users('ursula','stauder',23, 'santa cruz')

print(user1.reset_attempts())

print(user1.login_attempt())
print(user1.login_attempt())
print(user1.login_attempt())
print(user1.login_attempt())
print(user1.login_attempt())

user1.increment_login_attempts(50)

print(user1.reset_attempts())
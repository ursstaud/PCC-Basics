class Users:
	"""simple class example with users"""
	def __init__(self, first_name, last_name, age, location):
		self.first_name = first_name
		self.last_name = last_name
		self.age = age
		self.location = location

	def describe_user(self):
		"""describing the user example"""
		print(f"This user's full name is {self.first_name.title()} {self.last_name.title()}.")
		print(f"This user's age is {self.age}, and their location is in {self.location.title()}.")

	def greet_user(self):
		full_name = f"{self.first_name.title()} {self.last_name.title()}"
		print(f"Hello {full_name}, welcome!")


class Privileges:
	def __init__(self, privileges = ['can add post', 'can delete post', 'can ban user']): #list needs to be as default part of argument
		self.privileges = privileges

	def show_privileges(self):
		print(f"The admin has the following capabilities that normal users do not:")
		for privilege in self.privileges:
			print(f"-{privilege.title()}")


class Admin(Users):
	def __init__(self, first_name, last_name, age, location):
		super().__init__(first_name, last_name, age, location)
		self.privileges = Privileges()

admin1 = Admin('ursula', 'stauder', 23, 'santa cruz')

admin1.privileges.show_privileges()


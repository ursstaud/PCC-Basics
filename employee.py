class Employee:
	"""creating a profile of an employee"""
	def __init__(self, first, last, salary):
		self.first = first
		self.last = last
		self.salary = salary
		self.salaryincrease = 5000

	def give_raise(self):
		self.salary = self.salary + self.salaryincrease
		return self.salary



import unittest
from employee import Employee

class TestEmployee(unittest.TestCase):
	"""Test Employee Class"""

	def setUp(self):
		"""create employee"""
		#self.first = 'Ursula'
		#self.last = 'Stauder'
		#self.salary = 10000
		self.myself = Employee('Ursula', 'Stauder', 10000)

	def test_give_default_raise(self):
		self.myself.give_raise()
		self.assertEqual(self.myself.salary, 15000)

	def test_give_custom_raise(self):
		self.myself.salaryincrease=10000
		self.myself.give_raise()
		self.assertEqual(self.myself.salary, 20000)

if __name__ == '__main__':
	unittest.main()


import unittest
from city_functions import city_country

class CityTestCase(unittest.TestCase):
	"""Tests to make sure the function works"""

	def test_city_country(self):
		"""Do locations like Santiago, Chile work?"""
		formatted_country = city_country('santiago', 'chile')
		self.assertEqual(formatted_country, 'Santiago, Chile')

	def test_city_country_population(self):
		"""do locations with populations work?"""
		formatted_country = city_country('santiago', 'chile', 500)
		self.assertEqual(formatted_country, 'Santiago, Chile; Population: 500')

if __name__ == '__main__':
	unittest.main()
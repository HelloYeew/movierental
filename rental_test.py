import unittest
from datetime import datetime
from rental import Rental, PriceCode
from movie import *


class RentalTest(unittest.TestCase):
	
	def setUp(self):
		self.new_movie = Movie("Mulan", str(datetime.now().year), ["Children"])
		self.regular_movie = Movie("CitizenFour", "2005", ["Regular"])
		self.childrens_movie = Movie("Frozen", "2015", ["Children"])

	def test_movie_attributes(self):
		"""trivial test to catch refactoring errors or change in API of Movie"""
		m = Movie("AwesomeMovies", "2005", ["Regular"])
		self.assertEqual("AwesomeMovies", m.get_title())

	def test_rental_price(self):
		rental = Rental(self.new_movie, 1)
		self.assertEqual(rental.get_price(), 3)
		rental = Rental(self.new_movie, 5)
		self.assertEqual(rental.get_price(), 15)
		rental = Rental(self.regular_movie, 1)
		self.assertEqual(rental.get_price(), 2)
		rental = Rental(self.regular_movie, 4)
		self.assertEqual(rental.get_price(), 5)
		rental = Rental(self.childrens_movie, 3)
		self.assertEqual(rental.get_price(), 1.5)
		rental = Rental(self.childrens_movie, 5)
		self.assertEqual(rental.get_price(), 4.5)

	def test_rental_points(self):
		rental = Rental(self.new_movie, 1)
		self.assertEqual(rental.get_renter_point(), 1)
		rental = Rental(self.new_movie, 5)
		self.assertEqual(rental.get_renter_point(), 5)
		rental = Rental(self.regular_movie, 2)
		self.assertEqual(rental.get_renter_point(), 1)
		rental = Rental(self.regular_movie, 5)
		self.assertEqual(rental.get_renter_point(), 1)
		rental = Rental(self.childrens_movie, 1)
		self.assertEqual(rental.get_renter_point(), 1)
		rental = Rental(self.childrens_movie, 5)
		self.assertEqual(rental.get_renter_point(), 1)

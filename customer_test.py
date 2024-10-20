import re
import unittest 
from customer import Customer
from rental import Rental
from movie import MovieCatalog

class CustomerTest(unittest.TestCase): 
    """ Tests of the Customer class"""
    
    def setUp(self):
        """Test fixture contains:

        c = a customer
        movies = list of some movies
        """
        self.c = Customer("Movie Mogul")
        self.new_movie = MovieCatalog().get_movie("Dune: Part Two")
        self.regular_movie = MovieCatalog().get_movie("Deadpool")
        self.childrens_movie = MovieCatalog().get_movie("Mulan")

    def test_billing(self):
        """Test billing calculations for various rentals."""
        self.c.add_rental(Rental(self.new_movie, 2))
        self.c.add_rental(Rental(self.regular_movie, 3))
        self.c.add_rental(Rental(self.childrens_movie, 4))
        expected_total = (2 * 3.0 +2.0 + (3 - 2) * 1.5 +1.5 + (4 - 3) * 1.5)
        self.assertEqual(self.c.get_total_charge(), expected_total)

    def test_total_rental_points(self):
        """Test total rental points calculations for various rentals."""
        self.c.add_rental(Rental(self.new_movie, 3))
        self.c.add_rental(Rental(self.regular_movie, 2))
        self.c.add_rental(Rental(self.childrens_movie, 4))
        self.assertEqual(self.c.get_total_rental_points(), 5)

    def test_statement(self):
        stmt = self.c.statement()
        # get total charges from statement using a regex
        pattern = r".*Total [Cc]harges\s+(\d+\.\d\d).*"
        matches = re.match(pattern, stmt, flags=re.DOTALL)
        self.assertIsNotNone(matches)
        self.assertEqual("0.00", matches[1])
        # add a rental
        self.c.add_rental(Rental(self.new_movie, 4)) # days
        stmt = self.c.statement()
        matches = re.match(pattern, stmt.replace('\n',''), flags=re.DOTALL)
        self.assertIsNotNone(matches)
        self.assertEqual("12.00", matches[1])

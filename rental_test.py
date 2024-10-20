import unittest
from customer import Customer
from rental import Rental
from movie import MovieCatalog  # Assuming MovieCatalog is imported from the correct module


class RentalTest(unittest.TestCase):
    
    def setUp(self):
        self.new_movie = MovieCatalog().get_movie("Dune: Part Two")
        self.regular_movie = MovieCatalog().get_movie("Deadpool")
        self.childrens_movie = MovieCatalog().get_movie("Mulan")

    def test_movie_attributes(self):
        """Trivial test to catch refactoring errors or changes in the API of Movie"""
        movie = MovieCatalog().get_movie("Deadpool")
        self.assertEqual("Deadpool", movie.get_title())

    def test_rental_price(self):
        rental = Rental(self.new_movie, 1)
        self.assertEqual(rental.get_price(), 3.0)
        rental = Rental(self.new_movie, 5)
        self.assertEqual(rental.get_price(), 15.0)

        rental = Rental(self.regular_movie, 1)
        self.assertEqual(rental.get_price(), 2.0)
        rental = Rental(self.regular_movie, 4)
        self.assertEqual(rental.get_price(), 5.0)

        rental = Rental(self.childrens_movie, 1)
        self.assertEqual(rental.get_price(), 1.5)
        rental = Rental(self.childrens_movie, 4)
        self.assertEqual(rental.get_price(), 3.0)


    def test_rental_points(self):
        # Test new release earns points per day rented
        rental = Rental(self.new_movie, 3)
        self.assertEqual(rental.get_rental_points(), 3)

        # Test regular movie earns 1 point
        rental = Rental(self.regular_movie, 5)
        self.assertEqual(rental.get_rental_points(), 1)

        # Test children's movie earns 1 point
        rental = Rental(self.childrens_movie, 9)
        self.assertEqual(rental.get_rental_points(), 1)

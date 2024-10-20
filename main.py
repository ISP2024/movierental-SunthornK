# Demonstrate the movie rental code.
# Create a customer with some movies and print a statement.

from movie import Movie, MovieCatalog
from rental import Rental
from customer import Customer

def make_movies():
    """Some sample movies."""
    movies = [
        Movie("Air", Movie.NEW_RELEASE),
        Movie("Oppenheimer", Movie.REGULAR),
        Movie("Frozen", Movie.CHILDRENS),
        Movie("Bitconned", Movie.NEW_RELEASE),
        Movie("Particle Fever", Movie.REGULAR)
    ]
    return movies


if __name__ == '__main__':
    # Create a customer with some rentals
    customer = Customer("Edward Snowden")
    days = 5
    movie = MovieCatalog().get_movie("Ghost Light")
    # rental determines the price code itself
    rental = Rental(movie, days)
    # Add the rental to the customer
    customer.add_rental(rental)  # This line was missing
    # Print the statement
    print(customer.statement())


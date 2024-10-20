## Movie Rental Refactoring

A classic refactoring problem from Chapter 1 of
_Refactoring: Improving the Design of Existing Code_ by Martin Fowler.  

This repository contains Python code translated from the Java version.

The runnable `main.py` creates a customer and prints a statement.


## Instructions

See [Movie Rental Refactoring, Part 1](https://cpske.github.io/ISP/assignment/movierental/movierental-part1) for description of the code and what to do.

Before and after each refactoring you should **run the unit tests**.

## Resources

See [Resources](https://cpske.github.io/ISP/assignment/movierental/movierental-part1#resources) in the assignment description.

---
## Rationale

### 2.1 what refactoring signs (code smells) suggest this refactoring?
- Middle Man: The `Movie` class is acting as a middleman, only pass the requests to the pricing strategy.
- Low Cohesion: Price and points are related to the rental itself, not the movie. It makes more sense for these function to be in `Rental`.

### 2.2 what design principle suggests this refactoring? Why?
- Single Responsibility Principle (SRP): `Movie` should focus on movie data, while `Rental` handles pricing and points, since they are directly related to the rental process.

### 5.2 Where `price_code_for_movie` is Implemented and Why?
- I choose to implemented the `price_code_for_movie` on the `Movie` class because
  - Low Coupling: Keeping the pricing method in the Movie class means the Rental class doesn’t need to depend on it. 
   Then if we want to change how prices work we could do it without affecting the rental logic.
  - High Cohesion: The Movie class deals with movie details like the release year and genres. 
   Since the price code is based on these details, it makes sense to keep the method there.
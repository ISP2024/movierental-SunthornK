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
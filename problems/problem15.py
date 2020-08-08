import sys
import os

scriptpath = "../"
sys.path.append(os.path.abspath(scriptpath))

from util import factorial


if __name__ == "__main__":

    # You always have to go a set amount of times right and down.
    # The number of ways to do so is the how many combinations there are of those moves
    # => if you have to travel a 5x5 grid, how many strings exists that are made out of five 1(=right) and five 0(=down)

    # You can technically disregard one symbol and simply ask, for a AxB grid,
    # how many ways can you distribute A in A+B slots
    grid_dimension = 20

    # the combination of A in A+B slots is (A+B)! / !A * !(B-A)
    combinations = factorial.factorial(40)/(factorial.factorial(20) * factorial.factorial(20))

    print(combinations) # Isnt correct?

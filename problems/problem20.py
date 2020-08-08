import functools
import sys
import os

scriptpath = "../"
sys.path.append(os.path.abspath(scriptpath))

from util import factorial

if __name__ == "__main__":
    number = factorial.factorial(100)
    number_as_string = str(number)
    sum_of_digits = functools.reduce(lambda a , b: a+b, [int(digit) for digit in str(number)])
    print(sum_of_digits)

import os
import sys

scriptpath = "../"
sys.path.append(os.path.abspath(scriptpath))

from util import factorize


def find_largest_prime_factor(number):
    factorization = factorize.factorize_number(number)

    largest_prime, power = factorization[len(factorization)-1]
    return largest_prime


if __name__ == "__main__":
    prime = find_largest_prime_factor(600851475143)
    print(prime)

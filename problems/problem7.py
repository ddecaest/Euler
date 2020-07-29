import os
import sys

scriptpath = "../"
sys.path.append(os.path.abspath(scriptpath))

from primetest import miller_rabin


if __name__ == "__main__":
    number_of_primes_to_find = 10001
    number_of_primes_found = 0

    current_number = 2
    while number_of_primes_found < number_of_primes_to_find:
        if miller_rabin.prime_test(current_number, 40):
            number_of_primes_found += 1
        current_number += 1

    print(current_number-1)

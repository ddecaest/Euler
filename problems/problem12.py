import os
import sys

scriptpath = "../"
sys.path.append(os.path.abspath(scriptpath))

from util import factorize


def calculate_number_divisors(number):
    if number < 0:
        raise Exception("Input must be a positive number")
    if number == 0:
        # You can argue for either infinite or 0. Not really relevant...
        return 0

    factorization = factorize.CachedFactorizer().factorize_number(number)
    tally = 1
    for (prime_number, power) in factorization:
        tally = tally * (power+1)
    return tally


def generate_triangle_number(term_number):
    # 1 + 2 + 3 + 4 -> Arithmetic sequence
    return int(term_number * (term_number+1)/2)


if __name__ == "__main__":
    number_of_divisors_required = 500

    candidate_number = 1
    jump = 2
    candidate_divisors = calculate_number_divisors(candidate_number)

    while candidate_divisors < number_of_divisors_required:
        candidate_number += jump
        jump += 1

        candidate_divisors = calculate_number_divisors(candidate_number)

    print(str(candidate_number) + " -> " + str(candidate_divisors))

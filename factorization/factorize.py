import sys
import os

scriptpath = "../"
sys.path.append(os.path.abspath(scriptpath))
from primetest import miller_rabin

first_prime = 2


# Returns the prime factorization as list of tuples containing prime number - power, ordered from smallest prime to
# largest. For example 18 = 2*3*3, so it would return [(2,1),(3,2)]
def factorize_number(number):
    if number <= 0:
        return []
    if number == 1:
        # A bit of a weird case, 1 is technically not a prime number...
        return [(1, 1)]

    primes = []
    defactorized = number

    for factor_candidate in range(first_prime, number + 1):
        is_prime = miller_rabin.prime_test(factor_candidate, 40)
        if is_prime:
            power = 0
            while defactorized % factor_candidate == 0:
                power += 1
                defactorized = defactorized / factor_candidate
            if power != 0:
                primes.append((factor_candidate, power))

        if defactorized == 1:
            break

    return primes

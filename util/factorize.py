import sys
import os

scriptpath = "../"
sys.path.append(os.path.abspath(scriptpath))
from primetest import miller_rabin

first_prime = 2


class CachedFactorizer:
    cached_primes = [2]

    def factorize_number(self, number):
        if number <= 0:
            return []
        if number == 1:
            # A bit of a weird case, 1 is technically not a prime number...
            return [(1, 1)]

        primes = []
        defactorized = number

        for cached_prime in self.cached_primes:
            power, defactorized = _find_power_of_prime_divisor(cached_prime, defactorized)
            if power != 0:
                primes.append((cached_prime, power))
            if defactorized == 1:
                return primes

        biggest_cached_prime = self.cached_primes[len(self.cached_primes) - 1]
        for factor_candidate in range(biggest_cached_prime + 1, number + 1):
            is_prime = miller_rabin.prime_test(factor_candidate, 40)
            if is_prime:
                self.cached_primes.append(factor_candidate)

                power, defactorized = _find_power_of_prime_divisor(factor_candidate, defactorized)
                if power != 0:
                    primes.append((cached_prime, power))
                if defactorized == 1:
                    return primes

        return primes


def _find_power_of_prime_divisor(prime, number):
    defactorized = number
    power = 0
    while defactorized % prime == 0:
        power += 1
        defactorized = defactorized / prime

    return power, defactorized


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
            power, defactorized = _find_power_of_prime_divisor(factor_candidate, defactorized)
            if power != 0:
                primes.append((factor_candidate, power))
        if defactorized == 1:
            break

    return primes

import os
import sys

scriptpath = "../"
sys.path.append(os.path.abspath(scriptpath))

from prime import miller_rabin, sieve_of_eratothenes


def miller_rabin_way(up_to):
    tally = 0
    for i in range(2, up_to):
        if miller_rabin.miller_rabin_prime_test(i, 40):
            tally += i
    return tally


def sieve_way(up_to):
    primes = sieve_of_eratothenes.no_array_sieve_numbered_result_while_return_primes(up_to)
    sum = reduce(lambda x, y: x + y, primes)
    return sum


if __name__ == "__main__":
    up_to = 2000000

    print(miller_rabin_way(up_to))
    print(sieve_way(up_to))

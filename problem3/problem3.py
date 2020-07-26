import os
import sys

scriptpath = "../"
sys.path.append(os.path.abspath(scriptpath))

from prime import miller_rabin


def find_largest_prime_factor(number):
    if number == 0:
        return 0

    defactorized = number
    for i in range(2, number):
        is_prime = miller_rabin.miller_rabin_prime_test(i, 40)
        if is_prime:
            if i == defactorized:
                return i
            elif defactorized % i == 0:
                defactorized = defactorized / i

    return defactorized


if __name__ == "__main__":
    prime = find_largest_prime_factor(600851475143)
    print(prime)

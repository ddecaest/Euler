import os
import sys

scriptpath = "../"
sys.path.append(os.path.abspath(scriptpath))

from primetest import miller_rabin


def miller_rabin_way(up_to_input):
    tally = 0
    for i in range(2, up_to_input):
        if miller_rabin.prime_test(i, 40):
            tally += i
    return tally


if __name__ == "__main__":
    up_to = 2000000

    print(miller_rabin_way(up_to))

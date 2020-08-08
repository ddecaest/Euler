import functools
import sys
import os

scriptpath = "../"
sys.path.append(os.path.abspath(scriptpath))

from util import divisors


if __name__ == "__main__":

    sum_divisors_dict = {}
    for i in range(1, 10000):
        dividers = divisors.get_dividers(i)
        sum_divisors_dict[i] = functools.reduce(lambda a, b: a+b, dividers, 0)

    amicable_pairs = set()
    for a in list(sum_divisors_dict):
        da = sum_divisors_dict[a]
        dda = sum_divisors_dict.get(da, divisors.get_dividers(da))

        if a == dda and a != da:
            pair = None
            if a < da:
                pair = (a,da)
            else:
                pair = (da,a)
            amicable_pairs.add(pair)

    tally = 0
    for a,b in amicable_pairs:
        tally += a + b

    print(tally)

import functools
import sys
import os

scriptpath = "../"
sys.path.append(os.path.abspath(scriptpath))

from util import divisors


def calculate_abundant_numbers(up_to):
    abundant_numbers = []
    for i in range(1, up_to + 1):
        sum_divisors = functools.reduce(lambda a, b: a + b, divisors.get_dividers(i), 0)
        if sum_divisors > i:
            abundant_numbers.append(i)
    return abundant_numbers


if __name__ == "__main__":
    limit_of_sum_to_look_at = 28123

    abundant_numbers = calculate_abundant_numbers(limit_of_sum_to_look_at)
    number_of_abundant_numbers = len(abundant_numbers)

    sum_of_two_abundant_numbers = [False] * (limit_of_sum_to_look_at + 1)
    length_of_investigated_range = len(sum_of_two_abundant_numbers)

    for index, is_a_sum_of_abundant_numbers in enumerate(abundant_numbers):
        for index2 in range(index, number_of_abundant_numbers):
            sum_of_numbers = abundant_numbers[index] + abundant_numbers[index2]
            if sum_of_numbers < length_of_investigated_range:
                sum_of_two_abundant_numbers[sum_of_numbers] = True

    tally = 0
    for index, is_a_sum_of_abundant_numbers in enumerate(sum_of_two_abundant_numbers):
        if not is_a_sum_of_abundant_numbers:
            tally += index

    print(tally)

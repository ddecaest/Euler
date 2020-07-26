import math


def gauss_series(number_of_terms):
    return int(number_of_terms * (number_of_terms + 1) / 2)


def sum_squares(number_of_terms):
    tally = 0
    for i in range(1, number_of_terms + 1):
        tally += i * i
    return tally


if __name__ == "__main__":
    number_of_terms = 100

    square_of_sum = math.pow(gauss_series(number_of_terms), 2)
    sum_of_squares = sum_squares(number_of_terms)

    print(math.fabs(sum_of_squares - square_of_sum))

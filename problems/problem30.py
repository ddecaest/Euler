import math

if __name__ == "__main__":
    numbers_written_as_sum_of_fifth_power_digits = []

    fifth_powers = [math.pow(x, 5) for x in range(0, 10)]
    # Note: 9^5 7 times is still a 6 digit number, so the candidates are max 6 numbers long
    for i in range(2, 999999):
        digits = [int(d) for d in str(i)]

        sum_of_digits_to_fifth_power = sum([fifth_powers[digit] for digit in digits])
        if sum_of_digits_to_fifth_power == i:
            numbers_written_as_sum_of_fifth_power_digits += [i]

    print(sum(numbers_written_as_sum_of_fifth_power_digits))
def divisible_by_required_integers(number):
    if number == 0:
        return False

    return number % 11 == 0 and number % 12 == 0 and number % 13 == 0 \
           and number % 14 == 0 and number % 15 == 0 \
           and number % 16 == 0 and number % 17 == 0 \
           and number % 18 == 0 and number % 19 == 0 \
           and number % 20 == 0


if __name__ == "__main__":
    # Meh

    number = 0
    while not divisible_by_required_integers(number):
        number += 1

    print(number)

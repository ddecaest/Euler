

def tally_digits(number):
    tally = 0
    for digit in str(number):
        tally += int(digit)
    return tally


if __name__ == "__main__":
    number = 2 << 999
    print(tally_digits(number))
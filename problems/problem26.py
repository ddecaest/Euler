import decimal


def calculate_reciprocal_cycle(denominator):
    number = decimal.Decimal(1.0)/decimal.Decimal(denominator)

    if str(number).__contains__("."):
        decimals = str(number).split(".")[1]
    else:
        decimals = "0"

    nr_decimals = len(decimals)
    for i in range(2, nr_decimals//2):
        part1 = decimals[0:i]
        part2 = decimals[i:i*2]
        if part1 == part2:
            return len(part1)
    return 1

if __name__ == "__main__":
    decimal.getcontext().prec = 10000

    # Apparently, if:
    # - the denominator is not divisible by 2 or 5
    # - nominator and denominator don't share common factors other than 1 (always the case here)
    # Then the decimal representation is repeating
    denominators_to_consider = [number for number in range(1000) if number % 2 != 0 and number % 5 != 0]

    max_denominator, max_cycle_size = 0, 0
    for denominator in denominators_to_consider:
        cycle_size = calculate_reciprocal_cycle(denominator)
        if cycle_size > max_cycle_size:
            max_cycle_size = cycle_size
            max_denominator = denominator

    number = decimal.Decimal(1.0)/decimal.Decimal(max_denominator)
    print("result : " + str(max_denominator) + " " + str(max_cycle_size) + " " + str(number))
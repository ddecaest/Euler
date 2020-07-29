def tally_multiples_3_5(up_to_number):
    tally = 0

    for i in range(up_to_number):
        if i % 3 == 0 or i % 5 == 0:
            tally += i

    return tally


if __name__ == "__main__":
    print(tally_multiples_3_5(1000))

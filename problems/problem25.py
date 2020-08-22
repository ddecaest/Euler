if __name__ == "__main__":
    nr_digits = 1000

    previous = 1
    current = 1
    index = 2

    while len(str(current)) < 1000:
        next_current = current + previous
        previous = current
        current = next_current
        index += 1

    print(index)
    print(current)
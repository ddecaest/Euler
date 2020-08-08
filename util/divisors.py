
def get_dividers(number):
    dividers = []
    for i in range(1, int(number/2) + 1):
        if number % i == 0:
            dividers.append(i)
    return dividers

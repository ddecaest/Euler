

def factorial(number):
    tally = 1
    for i in range(2, number + 1):
        tally *= i
    return int(tally)

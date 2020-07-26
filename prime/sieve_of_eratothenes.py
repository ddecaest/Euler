def __prime_test(primes, number):
    for prime in primes:
        if number % prime == 0:
            return False
    return True


def no_array_sieve_numbered_result(number_prime_numbers):
    primes = []
    for i in range(2, 999999999999999):
        if __prime_test(primes, i):
            primes.append(i)
            if len(primes) == number_prime_numbers:
                return i
    return -1


def no_array_sieve_numbered_result_while(number_prime_numbers):
    primes = []
    i = 2
    while len(primes) != number_prime_numbers:
        if __prime_test(primes, i):
            primes.append(i)
        i += 1

    return primes


def no_array_sieve_numbered_result_while_return_primes(up_to):
    primes = []
    for i in range(2, up_to):
        if __prime_test(primes, i):
            primes.append(i)
    return primes

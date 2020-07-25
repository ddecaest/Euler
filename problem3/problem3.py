import random


def miller_rabin_prime_test(n, k):
    if n == 1:
        return False
    if n == 2 or n == 3:
        return True

    r, s = 0, n - 1
    while s % 2 == 0:
        r += 1
        s //= 2
    for _ in range(k):
        a = random.randrange(2, n - 1)
        x = pow(a, s, n)
        if x == 1 or x == n - 1:
            continue
        for _ in range(r - 1):
            x = pow(x, 2, n)
            if x == n - 1:
                break
        else:
            return False
    return True


def find_largest_prime_factor(number):
    if number == 0:
        return 0

    defactorized = number
    for i in range(2, number):
        is_prime = miller_rabin_prime_test(i, 40)
        if is_prime:
            if i == defactorized:
                return i
            elif defactorized % i == 0:
                defactorized = defactorized / i

    return defactorized


if __name__ == "__main__":
    prime = find_largest_prime_factor(600851475143)
    print(prime)
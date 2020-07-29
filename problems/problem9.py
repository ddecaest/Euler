def brute_force():
    for a in a_candidates:
        for b in b_candidates:
            for c in c_candidates:
                if not (a < b < c) or (a + b + c != 1000):
                    continue
                if a * a + b * b == c * c:
                    return a, b, c
    return -1, -1, -1


if __name__ == "__main__":
    a_candidates = range(1, 1000)
    b_candidates = range(1, 1000)
    c_candidates = range(1, 1000)

    a_result, b_result, c_result = brute_force()
    print(str(a_result) + " " + str(b_result) + " " + str(c_result))
    print(a_result * b_result * c_result)
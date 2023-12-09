if __name__ == "__main__":
    # 21 22 23 24 25
    # 20  7  8  9 10
    # 19  6  1  2 11
    # 18  5  4  3 12
    # 17 16 15 14 13

    # If spiral size in this case is 5
    # You have 4 diagonals of size 2, going NW, NE, SW, SE an the 1 in the middle

    spiral_size = 1001
    diagonal_size = spiral_size // 2 # So 500, for the problem

    # There is always a 1 in the middle
    sum = 1

    for i in range(1, diagonal_size + 1):
        # the NE diagonals are powers of 2, 3^2, 5^2, 7^2...
        base_nr = i*2 + 1
        ne_number = base_nr * base_nr

        # the NW diagonals are the same, but minus multiples of two
        nw_number = ne_number - i*2

        # in the very same way, the SW diagonals are the NW numbers minus multiples of two
        sw_number = nw_number - i*2

        # in the very very same way, the SE diagonals are the SW numbers minus multiples of two
        se_number = sw_number - i*2

        sum += nw_number
        sum += ne_number
        sum += sw_number
        sum += se_number

    print(sum)

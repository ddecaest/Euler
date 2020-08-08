pyramid = [
    [75],
    [95, 64],
    [17, 47, 82],
    [18, 35, 87, 10],
    [20, 4, 82, 47, 65],
    [19, 1, 23, 75, 3, 34],
    [88, 2, 77, 73, 7, 63, 67],
    [99, 65, 4, 28, 6, 16, 70, 92],
    [41, 41, 26, 56, 83, 40, 80, 70, 33],
    [41, 48, 72, 33, 47, 32, 37, 16, 94, 29],
    [53, 71, 44, 65, 25, 43, 91, 52, 97, 51, 14],
    [70, 11, 33, 28, 77, 73, 17, 78, 39, 68, 17, 57],
    [91, 71, 52, 38, 17, 14, 91, 43, 58, 50, 27, 29, 48],
    [63, 66, 4, 68, 89, 53, 67, 30, 73, 16, 69, 87, 40, 31],
    [4, 62, 98, 27, 23, 9, 70, 98, 73, 93, 38, 53, 60, 4, 23],
]


def get_best_path_score(pyramid):
    pyramid_transformed = pyramid

    while len(pyramid_transformed) > 1:
        number_of_rows = len(pyramid_transformed)
        # Each node in the second to last row is only reachable by the two nodes under it in the last row
        # So calculate the best way to reach it, then overwrite the alst node with that best total and pop the last row of the pyramid
        # If you keep doing this until only the first row is left, you will have determined the best path
        second_to_last_row = pyramid_transformed[number_of_rows - 2]
        last_row = pyramid_transformed[number_of_rows - 1]

        for i in range(0, len(second_to_last_row)):
            element = second_to_last_row[i]

            left_path_total = element + last_row[i]
            right_path_total = element + last_row[i + 1]

            if left_path_total > right_path_total:
                pyramid_transformed[number_of_rows - 2][i] = left_path_total
            else:
                pyramid_transformed[number_of_rows - 2][i] = right_path_total

        pyramid_transformed.pop()

    return pyramid_transformed[0][0]


if __name__ == "__main__":
    print(get_best_path_score(pyramid))

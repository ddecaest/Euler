from enum import Enum
import functools


class Direction(Enum):
    RIGHT = 0
    DOWN = 1
    DOWN_RIGHT = 2
    UP_RIGHT = 3

    def get_next(self):
        return Direction((self.value + 1) % 4)


class GridTraveller:

    def __init__(self, grid, sequence_length):
        self.grid = grid
        self.sequence_length = sequence_length
        self.x = 0
        self.y = 0
        self.direction = Direction(0)

        self.number_of_rows = len(self.grid)
        self.length_last_row = len(self.grid[self.number_of_rows - 1])

    def __has_next(self):
        reached_last_row = self.y == self.number_of_rows - 1
        reached_column_after_last_useful_column = self.x >= self.length_last_row - self.sequence_length
        return not (reached_last_row and reached_column_after_last_useful_column)

    def __get_number_of_columns_in_current_row(self):
        return len(self.grid[self.y])

    def next(self):
        sequence = None
        while sequence is None:
            if not self.__has_next():
                return None

            room_for_sequence_below = self.y <= self.number_of_rows - self.sequence_length
            room_for_sequence_right = self.x <= self.__get_number_of_columns_in_current_row() - self.sequence_length
            room_for_sequence_up = self.y >= self.sequence_length - 1

            if self.direction == Direction.DOWN:
                if room_for_sequence_below:
                    sequence = [self.grid[self.y + i][self.x] for i in range(0, self.sequence_length)]

            elif self.direction == Direction.RIGHT:
                if room_for_sequence_right:
                    sequence = [self.grid[self.y][self.x + i] for i in range(0, self.sequence_length)]

            elif self.direction == Direction.DOWN_RIGHT:
                if room_for_sequence_right and room_for_sequence_below:
                    sequence = [self.grid[self.y + i][self.x + i] for i in range(0, self.sequence_length)]

            elif self.direction == Direction.UP_RIGHT:
                if room_for_sequence_right and room_for_sequence_up:
                    sequence = [self.grid[self.y - i][self.x + i] for i in range(0, self.sequence_length)]

            else:
                raise Exception("Unknown direction: " + str(self.direction))

            self.direction = self.direction.get_next()

            if self.direction.value == 0:
                self.x += 1
                if self.x >= self.__get_number_of_columns_in_current_row():
                    self.y += 1
                    self.x = 0

        return sequence


if __name__ == "__main__":
    input_grid = [
        [8, 2, 22, 97, 38, 15, 00, 40, 00, 75, 4, 5, 7, 78, 52, 12, 50, 77, 91, 8],
        [49, 49, 99, 40, 17, 81, 18, 57, 60, 87, 17, 40, 98, 43, 69, 48, 4, 56, 62, 00],
        [81, 49, 31, 73, 55, 79, 14, 29, 93, 71, 40, 67, 53, 88, 30, 3, 49, 13, 36, 65],
        [52, 70, 95, 23, 4, 60, 11, 42, 69, 24, 68, 56, 1, 32, 56, 71, 37, 2, 36, 91],
        [22, 31, 16, 71, 51, 67, 63, 89, 41, 92, 36, 54, 22, 40, 40, 28, 66, 33, 13, 80],
        [24, 47, 32, 60, 99, 3, 45, 2, 44, 75, 33, 53, 78, 36, 84, 20, 35, 17, 12, 50],
        [32, 98, 81, 28, 64, 23, 67, 10, 26, 38, 40, 67, 59, 54, 70, 66, 18, 38, 64, 70],
        [67, 26, 20, 68, 2, 62, 12, 20, 95, 63, 94, 39, 63, 8, 40, 91, 66, 49, 94, 21],
        [24, 55, 58, 5, 66, 73, 99, 26, 97, 17, 78, 78, 96, 83, 14, 88, 34, 89, 63, 72],
        [21, 36, 23, 9, 75, 00, 76, 44, 20, 45, 35, 14, 00, 61, 33, 97, 34, 31, 33, 95],
        [78, 17, 53, 28, 22, 75, 31, 67, 15, 94, 3, 80, 4, 62, 16, 14, 9, 53, 56, 92],
        [16, 39, 5, 42, 96, 35, 31, 47, 55, 58, 88, 24, 00, 17, 54, 24, 36, 29, 85, 57],
        [86, 56, 00, 48, 35, 71, 89, 7, 5, 44, 44, 37, 44, 60, 21, 58, 51, 54, 17, 58],
        [19, 80, 81, 68, 5, 94, 47, 69, 28, 73, 92, 13, 86, 52, 17, 77, 4, 89, 55, 40],
        [4, 52, 8, 83, 97, 35, 99, 16, 7, 97, 57, 32, 16, 26, 26, 79, 33, 27, 98, 66],
        [88, 36, 68, 87, 57, 62, 20, 72, 3, 46, 33, 67, 46, 55, 12, 32, 63, 93, 53, 69],
        [4, 42, 16, 73, 38, 25, 39, 11, 24, 94, 72, 18, 8, 46, 29, 32, 40, 62, 76, 36],
        [20, 69, 36, 41, 72, 30, 23, 88, 34, 62, 99, 69, 82, 67, 59, 85, 74, 4, 36, 16],
        [20, 73, 35, 29, 78, 31, 90, 1, 74, 31, 49, 71, 48, 86, 81, 16, 23, 57, 5, 54],
        [1, 70, 54, 71, 83, 51, 54, 69, 16, 92, 33, 48, 61, 43, 52, 1, 89, 19, 67, 48]
    ]

    traveller = GridTraveller(input_grid, 4)

    highest_so_far = 0

    next_sequence = traveller.next()
    while next_sequence is not None:
        product = functools.reduce(lambda x, y: x * y, next_sequence)
        if product > highest_so_far:
            highest_so_far = product

        next_sequence = traveller.next()

    print(highest_so_far)

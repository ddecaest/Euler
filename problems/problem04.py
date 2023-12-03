import math


class DigitCoupleGenerator:
    first = 999
    second = 999

    def get_next_couple(self):
        to_return = self.first, self.second

        self.first -= 1

        if self.first == 100 and self.second == 100:
            return -1, -1
        elif self.first == 99:
            self.first = 999
            self.second -= 1

        return to_return


def is_palindrome(integer):
    stringy_integer = str(integer)
    number_digits = len(stringy_integer)

    for i in range(math.floor(number_digits/2)):
        if stringy_integer[i] != stringy_integer[number_digits - i - 1]:
            return False
    return True


if __name__ == "__main__":
    generator = DigitCoupleGenerator()

    max_palindrome = 0
    first, second = generator.get_next_couple()
    while (first, second) != (-1, -1):
        if is_palindrome(first*second) and first*second > max_palindrome:
            max_palindrome = first*second
        first, second = generator.get_next_couple()

    print(max_palindrome)

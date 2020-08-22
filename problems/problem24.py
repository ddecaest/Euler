import sys
import os

scriptpath = "../"
sys.path.append(os.path.abspath(scriptpath))


class PermutationNumber:
    def __init__(self):
        self.lowest = 123456789
        self.highest = 9876543210
        self.permutation_index_nr = -1
        self.next = None

    @staticmethod
    def is_permutation(number):
        stringy = str(number)

        one_to_nine = "1" in stringy and "2" in stringy and "3" in stringy and "4" in stringy \
                      and "5" in stringy and "6" in stringy and "7" in stringy and "8" in stringy and "9" in stringy

        if len(stringy) == 9 and one_to_nine:
            return True
        elif len(stringy) == 10 and one_to_nine and "0" in stringy:
            return True
        else:
            return False

    def get_next(self):
        if self.next is None:
            self.next = self.lowest
        else:
            self.next += 1
            while not self.is_permutation(self.next):
                self.next += 1

                if self.next > self.highest:
                    raise Exception("I reached the maximum!")

        self.permutation_index_nr += 1
        return self.next


if __name__ == "__main__":
    index_to_look_for = 999999

    permutation_number = PermutationNumber()
    while permutation_number.permutation_index_nr != index_to_look_for:
        permutation_number.get_next()

    print(permutation_number.next)

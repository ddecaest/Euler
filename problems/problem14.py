class CachedCollatzSequenceLengthCounter:
    cached_numbers = {}

    @staticmethod
    def __get_next_in_sequence(number):
        if number % 2 == 0:
            return number/2
        else:
            return 3 * number + 1

    def count_length(self, sequence_start):
        sequence_number_in_progress = sequence_start
        sequence_length = 1

        while sequence_number_in_progress != 1:
            if sequence_number_in_progress in self.cached_numbers:
                sequence_length += self.cached_numbers[sequence_number_in_progress]
                sequence_number_in_progress = 1
            else:
                sequence_length += 1
                sequence_number_in_progress = self.__get_next_in_sequence(sequence_number_in_progress)

        self.cached_numbers[sequence_start] = sequence_length
        return sequence_length


if __name__ == "__main__":
    sequence_length_counter = CachedCollatzSequenceLengthCounter()
    longest_sequence = 1
    longest_starting_number = 1

    for i in range(2, 1000000):
        i_length = sequence_length_counter.count_length(i)
        if i_length > longest_sequence:
            longest_sequence = i_length
            longest_starting_number = i

    print(str(longest_starting_number) + " -> " + str(longest_sequence))
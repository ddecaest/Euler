class FibonacciGenerator:
    first_number = 0
    second_number = 1

    def generate_next_number(self):
        next_number = self.first_number + self.second_number
        self.first_number = self.second_number
        self.second_number = next_number

        return next_number


def tally_even_fibonacci(up_to_number):
    tally = 0
    fibonacci_number = generator.generate_next_number()
    while fibonacci_number < up_to_number:
        if fibonacci_number % 2 == 0:
            tally += fibonacci_number
        fibonacci_number = generator.generate_next_number()
    return tally


if __name__ == "__main__":
    generator = FibonacciGenerator()

    print(tally_even_fibonacci(4000000))

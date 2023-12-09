import math

if __name__ == "__main__":
    set_of_numbers = set()
    for a in range(2, 101):
        for b in range(2, 101):
            set_of_numbers.add(math.pow(a, b))
    print(len(set_of_numbers))
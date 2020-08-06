special_cases_dict = [
    "zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine", "ten",
    "eleven", "twelve", "thirteen", "fourteen", "fifteen", "sixteen", "seventeen", "eighteen", "nineteen"
]
names_of_tens = ["zero", "ten", "twenty", "thirty", "forty", "fifty", "sixty", "seventy", "eighty", "ninety"]


def get_number_as_words(number):
    number_stringified = str(number)
    number_as_words = ""
    original_number_of_digits = len(number_stringified)
    while len(number_stringified) > 0:
        digit_parsed = int(number_stringified[0])
        current_number_of_digits = len(number_stringified)

        if digit_parsed == 0:
            number_stringified = number_stringified[1:]
        elif current_number_of_digits == 4:
            number_as_words += special_cases_dict[digit_parsed] + " thousand"
            number_stringified = number_stringified[1:]
        elif current_number_of_digits == 3:
            number_as_words += special_cases_dict[digit_parsed] + " hundred"
            number_stringified = number_stringified[1:]
        elif current_number_of_digits <= 2:
            if original_number_of_digits > 2:
                number_as_words += " and "

            if int(number_stringified) < 20:
                number_as_words += special_cases_dict[int(number_stringified)]
            else:
                tens_digit = int(number_stringified[0])
                single_digit = int(number_stringified[1])
                number_as_words += names_of_tens[tens_digit]

                if single_digit != 0:
                    number_as_words += "-" + special_cases_dict[single_digit]

            number_stringified = number_stringified[2:]
        else:
            raise Exception("Number with " + str(current_number_of_digits) + " digits are not supported!")

    return number_as_words


if __name__ == "__main__":
    tally = 0
    for i in range(1, 1000 + 1):
        as_words = get_number_as_words(i)
        with_extra_chars_removed = as_words.replace(" ", "").replace("-", '')
        print(with_extra_chars_removed)
        tally += len(with_extra_chars_removed)

    print(tally)
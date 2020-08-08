class MyDate:
    def __init__(self, day, month, year, type_of_day):
        self.day_index = day
        self.month_index = month
        self.type_of_day = type_of_day
        self.year = year

    def is_leap_year(self):
        return (self.year % 4 == 0 and self.year % 100 != 0) or self.year % 400 == 0

    def get_days_in_current_month(self):
        # February(=1) is a mess...
        if self.month_index == 1:
            if self.is_leap_year():
                return 29
            else:
                return 28
        if self.month_index in [0, 2, 4, 6, 7, 9, 11]:
            return 31
        else:
            return 30

    def add_days(self, days_to_add):
        self.day_index += days_to_add
        self.type_of_day = (self.type_of_day + days_to_add) % 7

        while self.day_index >= self.get_days_in_current_month():
            self.day_index -= self.get_days_in_current_month()
            self.month_index += 1
            if self.month_index > 11:
                self.month_index = 0
                self.year += 1

    def __lt__(self, other):
        if self.year != other.year:
            return self.year < other.year
        if self.month_index != other.month_index:
            return self.month_index < other.month_index
        return self.day_index < other.day_index

    def __le__(self, other):
        return (self.year == other.year and self.month_index == other.month_index and self.day_index == other.day_index) \
               or self < other

    def __str__(self):
        return str(self.day_index + 1) + "/" + str(self.month_index + 1) + "/" + str(self.year) + " (type of day: " + str(self.type_of_day) + " )"


if __name__ == "__main__":
    current_date = MyDate(0, 0, 1900, 0)
    start_date = MyDate(0, 0, 1901, -1)
    end_date = MyDate(30, 11, 2000, -1)

    while current_date < start_date:
        current_date.add_days(1)

    number_of_sundays = 0

    # Move to first sunday
    while current_date.type_of_day != 6:
        current_date.add_days(1)

    # Iterate over sundays by adding 7 days until we pass the end_date
    while current_date <= end_date:
        if current_date.day_index == 0:
            number_of_sundays += 1

        current_date.add_days(7)

    print(number_of_sundays)

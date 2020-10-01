class Date:
    weekdays = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
    days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

    def __init__(self, day, month, year):
        self.day = day
        self.month = month
        self.year = year

    @property
    def weekday(self):
        origin = Date(1, 1, 1900)
        days = 0
        for year in range(self.year - origin.year):
            days += sum(Date.days)
            if year % 4 == 0 and (year % 100 != 0 or year % 400 == 0):
                days += 1
        for month in range(self.month - origin.month):
            days += self.days[month]
        if self.year % 4 == 0 and (self.year % 100 != 0 or self.year % 400 == 0):
            days += 1
        days += self.day - origin.day
        return self.weekdays[days % 7]
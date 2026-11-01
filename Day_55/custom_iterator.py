
# Day 55: Custom Iterator

class CountUp:

    def __init__(self, limit):
        self.current = 1
        self.limit = limit

    def __iter__(self):
        return self

    def __next__(self):

        if self.current <= self.limit:
            value = self.current
            self.current += 1
            return value

        raise StopIteration


counter = CountUp(5)

for number in counter:
    print(number)

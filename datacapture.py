class Stats:
    def __init__(self):
        self.data = {}
        self.max_number = 0
        self.min_number = 0

    def less(self, number):
        result = 0
        for _ in range(self.min_number, number):
            result += self.data.get(_, 0)
        return result

    def between(self, from_n, to_n):
        result = 0
        start = from_n if from_n < to_n else to_n
        end = from_n if from_n > to_n else to_n
        for _ in range(start, end + 1):
            result += self.data.get(_, 0)
        return result

    def greater(self, n):
        result = 0
        for _ in range(n + 1, self.max_number + 1):
            result += self.data.get(_, 0)
        return result


class DataCapture:
    def __init__(self):
        self.stats = Stats()
        self.raw_data = []
        self.bof = False

    def add(self, number):
        """Add item to raw data set or send to stats directly in case of bof (build on the fly)"""
        if self.bof:
            self.check_min_max(number)
            self.stats.data.update({number: self.stats.data.get(number, 0) + 1})
        else:
            self.raw_data.append(number)

    def build_stats(self):
        """Build stat data set"""
        if self.bof:
            return self.stats

        for n in self.raw_data:
            self.check_min_max(n)
            self.stats.data.update({n: self.stats.data.get(n, 0) + 1})

        self.raw_data = []
        return self.stats

    def check_min_max(self, n):
        if self.stats.max_number < n:
            self.stats.max_number = n
        if self.stats.min_number > n:
            self.stats.min_number = n

    def build_on_fly(self, val):
        """Building stats every time that is added it's also possible"""
        # using an inline if to support 0,1 and Booleans
        if self.raw_data:
            self.build_stats()
        self.bof = True if val else False

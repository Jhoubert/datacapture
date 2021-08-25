class Stats:
    def __init__(self):
        self.data = {}
        self.max_number = 0
        self.min_number = 0

    def less(self, number):
        if number < self.min_number:
            return 0
        elif number > self.max_number:
            return self.data.get(self.max_number, 0)
        else:
            return self.data.get(number - 1, 0)

    def between(self, from_n, to_n):

        start = self.min_number if from_n < self.min_number else from_n
        end = self.max_number if to_n > self.max_number else to_n

        result = self.data.get(end, 0) - self.data.get(start - 1, 0)
        return result

    def greater(self, number):
        if number < self.min_number:
            self.data.get(self.max_number, 0)
        elif number > self.max_number:
            return 0
        else:
            return self.data.get(self.max_number, 0) - self.data.get(number, 0)


class DataCapture:
    def __init__(self):
        self.stats = Stats()
        self.raw_data = {}

    def add(self, number):
        """Add item to raw data set"""
        self.check_min_max(number)
        self.raw_data.update({number: self.raw_data.get(number, 0) + 1})

    def build_stats(self):
        """Build stat data set"""
        result_i = 0
        last = 0
        for n in range(self.stats.min_number, self.stats.max_number + 1):
            result_i += self.raw_data.get(n, 0)
            self.stats.data.update({n: result_i})

        return self.stats

    def check_min_max(self, n):
        if self.stats.max_number < n:
            self.stats.max_number = n
        if self.stats.min_number > n:
            self.stats.min_number = n

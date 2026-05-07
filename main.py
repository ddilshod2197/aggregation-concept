class Aggregation:
    def __init__(self, data):
        self.data = data

    def sum(self):
        return sum(self.data)

    def average(self):
        return sum(self.data) / len(self.data)

    def max(self):
        return max(self.data)

    def min(self):
        return min(self.data)

    def count(self):
        return len(self.data)


class Aggregator:
    def __init__(self, data):
        self.data = data

    def aggregate(self, aggregation_type):
        if aggregation_type == 'sum':
            return Aggregation(self.data).sum()
        elif aggregation_type == 'average':
            return Aggregation(self.data).average()
        elif aggregation_type == 'max':
            return Aggregation(self.data).max()
        elif aggregation_type == 'min':
            return Aggregation(self.data).min()
        elif aggregation_type == 'count':
            return Aggregation(self.data).count()
        else:
            return "Bunday agregatsiya turi yo'q"


# Test qilish
data = [1, 2, 3, 4, 5]
aggregator = Aggregator(data)
print(aggregator.aggregate('sum'))  # 15
print(aggregator.aggregate('average'))  # 3.0
print(aggregator.aggregate('max'))  # 5
print(aggregator.aggregate('min'))  # 1
print(aggregator.aggregate('count'))  # 5
print(aggregator.aggregate('boshqa'))  # Bunday agregatsiya turi yo'q

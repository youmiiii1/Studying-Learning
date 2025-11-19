# Example - 1
class Indexer:
    def __init__(self, iterable: str, start = 0):
        self.iterable = iter(iterable)
        self.index = start

    def __iter__(self):
        return self

    def __next__(self):
        item = next(self.iterable)
        current_index = self.index
        self.index += 1
        return (current_index, item)

for i, val in Indexer(["a", "b", "c"], start=1):
    print(i, val)

# Example - 2
class Counter:
    def __init__(self, number_end: int, start_number: int, step_number: int):
        if step_number == 0:
            raise ValueError
        self.number_end = number_end
        self.start_number = start_number
        self.step_number = step_number

    def __iter__(self):
        return self

    def __next__(self):
        if self.start_number >= self.number_end:
            raise StopIteration
        value = self.start_number
        self.start_number += self.step_number
        return value


c = Counter(100, 2, 5)
for num in c:
    print(num)

# Example - 3
class MyIterable:
    def __init__(self):
        self.data = [1, 2, 3, 4]

    def __iter__(self):
        return iter(self.data)

    def __getitem__(self, index):
        return self.data[index]

c = MyIterable()
for item in c:
    print(item)
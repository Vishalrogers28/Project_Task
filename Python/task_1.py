class Rectangle:
    def __init__(self, length: int, width: int):
        self.length = length
        self.width = width

    def __iter__(self):
        self._iter_data = iter([{'length': self.length}, {'width': self.width}])
        return self

    def __next__(self):
        return next(self._iter_data)


rect = Rectangle(5, 10)
for dimension in rect:
    print(dimension)

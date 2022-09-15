"""Custom Generators"""

class iterator:
    def __init__(self,start,end):
        self.start = start
        self.end = end

    def __next__(self):
        if self.start >= self.end:
            raise StopIteration
        current_val = self.start
        self.start += 1
        return current_val

class iterator_and_iterable:
    def __init__(self,start,end):
        self.start = start
        self.end = end

    def __next__(self):
        if self.start >= self.end:
            raise StopIteration
        current_val = self.start
        self.start += 1
        return current_val

    def __iter__(self):
        return self

obj_iterator = iterator(1,10)
print(next(obj_iterator))
print(obj_iterator.__next__())

obj_iterator_and_iterable = iterator_and_iterable(1,5)
print(next(obj_iterator_and_iterable))
for i in obj_iterator_and_iterable:
    print(i)

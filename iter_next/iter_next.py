class humnum:
    def __init__(self):
        self.x = 0
    def __next__(self):
        if self.x < 100:
            self.x += 1
            return self.x
        else:
            raise StopIteration()
    def __iter__(self):
        return self

# class fun_iter:
#     def __iter__(self):
#         return humnum()

ob = humnum()
iter_val = iter(ob)
for i in iter_val:
    print(i)






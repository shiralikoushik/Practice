from contextlib import contextmanager
from fnmatch import fnmatch
@contextmanager
def open_file(f_name,mode):
    f = open(f_name,mode)
    return f
    f.close()


with open_file("text.txt","w") as f:
    f.write("Hi this is example of context manager")

print(f.closed)
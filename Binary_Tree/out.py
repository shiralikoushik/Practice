from operator import imod
print(__name__)

from parent1 import par
from child1 import chi
x = chi(par(5))

print(x)

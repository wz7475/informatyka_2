import math
from random import randint
def in_circle(x, y):
    if math.sqrt(x *x + y*y) <= 1:
        return 1
    return 0

tab = []
total_in = 0

for i in range(100):
    point = []
    point.append(randint(0, 100) / 100)
    point.append(randint(0, 100) / 100)
    tab.append(point)

for i in tab:
    print(i)
    total_in += in_circle(i[0], i[1])

print(100.0 / total_in)

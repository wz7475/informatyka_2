import math
for i in range(3, 21):
    k = int(math.floor(i / 2))
    x = int(math.pow(2, k) * math.factorial(k))
    print(str(i) + ": " + str(x))
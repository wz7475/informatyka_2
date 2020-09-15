for i in range(21):
    x = (i*i + i +1) * (i*i  - i + 1)
    output = str(i) + ": " + str(x) + " " + str(x % 12)
    print(output) 
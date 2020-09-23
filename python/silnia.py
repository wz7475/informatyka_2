from math import factorial
tab = []

x = factorial(int(input("enter number:\n")))
x = str(x)
for i in x:
    tab.append(int(i))

print(x)

tab = tab[::-1]
for i in tab:
    if i != 0:
        print(i)
        break
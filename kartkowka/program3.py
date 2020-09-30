x = int(input("podaj liczbe: "))
if x % 2 == 0:
    start = 2
else:
    start = 3
suma = 1
for i in range(start, x+1, 2):
    suma *= i

print(suma)
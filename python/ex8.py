n = int(input("enter n:\n"))
suma = 1
for i in range(2, n+1):
    if i % 2 == 0:
        suma += 1 / i
    else:
        suma -= 1 / i

print(suma)
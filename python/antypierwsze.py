def amount_factors(x):
    factors = []
    for i in range(1, x+1):
        if x % i == 0:
            factors.append(i)
    return len(factors)

def antifirst(x):
    for i in range(1, x):
        if amount_factors(i) >= amount_factors(x):
            return False
    return True

n = int(input("enter number:\n"))
suma = 0

for i in range(1, n +1):
    if antifirst(i):
        suma += i
        print(i)

#print(suma)
#print(antifirst(n))
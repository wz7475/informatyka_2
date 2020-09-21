tab = [1, 3,7, 9, 1, 3, 7, 9, 1,3]
p = []
suma = 0
pesel = input("enter pesel:\n")
for i in pesel:
    p.append(int(i))

for i in range(10):
    suma += p[i] * tab[i]

rest = suma % 10
control_sum = 10 - rest
if rest == 0:
    control_sum = 0

if control_sum != p[10] and control_sum != 0:
    print("incorrect data")
else:
    if p[9] % 2 == 0:
        print("women")
    else:
        print("man")
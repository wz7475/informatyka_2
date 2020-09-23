from sys import exit

x = int(input("enter number:\n"))
y = str(x)
length = len(y)
sum_1 = 0
sum_2 = 0

if len(y) % 2 != 0:
    print("not happy")
    exit()

for i in range(int(length / 2)):
    sum_1 += int(y[i])

for i in range(int(length / 2), length):
    sum_2 += int(y[i])

print(sum_1)
print(sum_2)

if sum_1 == sum_2:
    print("happy")
else:
    print("not happy")


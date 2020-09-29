x = int(input("enter number: "))
sum = 1
if x % 2 == 0:
    start = 2
else:
    start = 3
for i in range(start, x + 1, 2):
    sum *= i

print(sum)
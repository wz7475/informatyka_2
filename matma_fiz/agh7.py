from itertools import permutations
n = int(input("enter n:\n"))
#n = 4
tab = []
score = []
for i in range(1, 1+n):
    tab.append(i)

p = permutations(tab)
for i in p:
    length = len(i)
    suma = i[0] + i[-1]
    j = 0
    condition = True
    while(j < length/2):
        if i[j] + i[length - j - 1] != suma:
            condition = False
            break
        j += 1
    if condition:
        score.append(i)


print(len(score))
for i in score:
    print(i)
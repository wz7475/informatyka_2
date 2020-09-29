from math import floor
n = int(input("enter n: "))
weight = int(input("enter weight: "))
print("enter weights and values:")
w = [] 
v = []
a = []
for i in range(n):
    w.append(int(input("weight: ")))
    v.append(int(input("value: ")))
score = 0
for i in range(n):
    a.append(int(floor(weight/w[i])))
    weight -= a[i] * w[i]
    score += v[i] * a[i]
print(score)
for i in range(n):
    if a[i] != 0:
        print("amount: {score}".format(score = a[i]))
        print("value: {score}".format(score = v[i]))
        print("weight: {score}".format(score = w[i]))
        print()
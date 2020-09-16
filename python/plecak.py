weight = int(input("enter max weight of backpack: "))
n = int(input("enter amount of items: "))

v = []
w = []
a = []
score = 0

for i in range(n):
    v.append(int(input("enter value: ")))
    w.append(int(input("enter weight: ")))

def pack_backpack(a, w, v):
    global score
    global weight
    for i in range(n):
        a.append(weight / w[i])
        weight -= a[i] * w[i]
        score += a[i] * v[i]
pack_backpack(a, w, v)
print("\nvalue of packed items: {score}".format(score = score))
for i in range(n):
    if a[i] != 0:
        print("amount: {a[i]}")
        print("value: {v[i]}")
        print("weight: {w[i]}")
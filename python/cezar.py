alphabet = "abcdefghijklmnoprstuwzxyz"

""" s = input("enter word: ")
key = int(input("enter key: "))
 """
s = "abcd"
key = 5
new = ""

for i in s:
    #print(ord(i))
    #print((ord(i) + key) % 93 + 97)
    i = (chr((ord(i) + key) % 93 + 93))
    new += i
    
print(new)
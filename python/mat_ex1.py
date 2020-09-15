import os

same_length = []

with open(os.path.join("text_files", "anagram.txt")) as f:
    tab = f.readlines()

for i in tab:
    words = i.split(" ")
    words[-1].pop()
    words[-1].pop()
    length = len(words[0])
    if len(words[0]) == len(words[1]) == len(words[2]) == len(words[3]) == len(words[4]):
        same_length.append(i)

for i in same_length:
    print(i)


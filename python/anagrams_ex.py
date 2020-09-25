import os

same_length = []
anagrams = []

def anagram(s1, s2):
    if "".join(sorted(s1)) == "".join(sorted(s2)):
        return True
    return False

with open(os.path.join("text_files", "anagram.txt")) as f:
    tab = f.readlines()

for i in tab:
    words = i.split(" ")
    """ words[-1].pop()
    words[-1].pop() """
    words[-1] = words[-1][:-1]
    if len(words[0]) == len(words[1]) == len(words[2]) == len(words[3]) == len(words[4]):
        same_length.append(i)

for i in same_length:
    condition = True
    words = i.split(" ")
    words[-1] = words[-1][:-1]
    for j in words:
        condition = anagram(words[0], j)
        if condition == False:
            break
    if condition:
        anagrams.append(i)

with open(os.path.join("text_files", "same_length.txt"), "w") as f:
    f.writelines(same_length)

with open(os.path.join("text_files", "only_anagrams.txt"), "w") as f:
    f.writelines(anagrams)
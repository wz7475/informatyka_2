s1 = input("wprowadz wyraz: ")
s2 = input("wprowadz wyraz: ")

def anagram(s1, s2):
    if len(s1) != len(s2):
        return False
    if "".join(sorted(s1)) != "".join(sorted(s2)):
        return False
    return True

if anagram(s1, s2):
    print("sa anagramami")
else:
    print("nie sa anagramami")
s = input("podaj wyraz (male litery): ")
alphabet = "abcdefghijklmnopqrstuvxyw"
new_word = ""
for i in range(len(s)):
    index = (alphabet.index(s[i]) + 3) % len(alphabet)
    print(index)
    new_word += alphabet[index]
print(new_word)
alphabet = "abcdefghijklmnoprstwyz"

key = int(input("enter key:\n"))

word = input("enter word:\n")
new_word = ""
for i in range(len(word)):
    index_in_alphabet = alphabet.index(word[i])
    new_word += alphabet[(index_in_alphabet + key)% len(alphabet)]
    

print(new_word)
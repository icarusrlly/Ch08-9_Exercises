def is_palindrome(word):
    word = word.lower()
    return word == ''.join(reversed(word))

fin = open('words.txt', 'r', encoding='utf-8')
word_list = []
for line in fin:
    word_list.append(line.strip())
fin.close()

for word in word_list:
    if len(word) >= 7 and is_palindrome(word):
        print(word)

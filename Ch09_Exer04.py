def total_length(word_list):
    return sum(len(word) for word in word_list)

word_list = []
fin = open('words.txt', 'r', encoding='utf-8')

for line in fin:
    word = line.strip()  # .strip() removes the newline character (\n)
    word_list.append(word)
fin.close()
result = total_length(word_list)
print(result)


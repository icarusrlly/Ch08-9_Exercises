import urllib.request

url = "https://raw.githubusercontent.com/AllenDowney/ThinkPython2/master/code/words.txt"

response = urllib.request.urlopen(url)
content = response.read().decode('utf-8')

f = open('words.txt', 'w', encoding='utf-8')
f.write(content)
f.close()

print("words.txt created successfully with UTF-8 encoding!")

def is_anagram(word1, word2):
    return sorted(word1.lower()) == sorted(word2.lower())

target = "takes"
anagrams = []

fin = open('words.txt', 'r', encoding='utf-8')

for line in fin:
    word = line.strip().lower()
    if word != target and is_anagram(word, target):
        anagrams.append(word)

fin.close()
print(f"Anagrams of '{target}': {anagrams}")

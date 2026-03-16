def avoids(word, forbidden):
    for letter in word:
        if letter in forbidden:
            return False
    return True

def uses_all(word, required):
    for letter in required:
        if letter not in word:
            return False
    return True


def check_word(word):
    if 'e' not in word or 'm' not in word:
        return False
    if word[4] != 'm':
        return False
    if word[2] == 'e' or word[3] == 'e' or word[4] == 'e':
        return False
    forbidden = "spadclrkto"
    for letter in word:
        if letter in forbidden:
            return False
    return True

#  --- Running the code ---
word_list = ['tenet', 'theme', 'begin', 'tweet', 'biome']
valid_words = []

for word in word_list:
     if check_word(word):
         valid_words.append(word)

print(f"Possible target words: {valid_words}")
print(f"Total count: {len(valid_words)}")
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
    if not uses_all(word, 'e'):
        return False
    if word[4] == 'e' or word[2] == 'e':
        return False
    if not avoids(word, 'spadclrk'):
        return False
    return True

# --- Running the code ---
word_list = ['tenet', 'theme', 'begin', 'tweet', 'biome', 'eight']
valid_words = []

for word in word_list:
    if check_word(word):
        valid_words.append(word)

print(f"Possible target words: {valid_words}")
print(f"Total count: {len(valid_words)}")

def reverse_sentence(sentence):
    words = sentence.split()
    reversed_words = reversed(words)
    new_sentence = " ".join(reversed_words)
    return new_sentence.capitalize()

result = reverse_sentence("Reverse this sentence")
print(result)

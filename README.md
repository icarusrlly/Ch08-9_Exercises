# Ch08-9_Exercises

# 8.12.2. Exercise
# See if you can write a function that does the same thing as the shell command !head. It should take as arguments the name of a file to read, the number of lines to read, and the name of the file to write the lines into. If the third parameter is None, it should display the lines rather than write them to a file.

# 8.12.3. Exercise
# “Wordle” is an online word game where the objective is to guess a five-letter word in six or fewer attempts. Each attempt has to be recognized as a word, not including proper nouns. After each attempt, you get information about which of the letters you guessed appear in the target word, and which ones are in the correct position.
# For example, suppose the target word is MOWER and you guess TRIED. You would learn that E is in the word and in the correct position, R is in the word but not in the correct position, and T, I, and D are not in the word.
# As a different example, suppose you have guessed the words SPADE and CLERK, and you’ve learned that E is in the word, but not in either of those positions, and none of the other letters appear in the word. Of the words in the word list, how many could be the target word? Write a function called check_word that takes a five-letter word and checks whether it could be the target word, given these guesses.
# You can use any of the functions from the previous chapter, like uses_any.

# 8.12.4. Exercise
# Continuing the previous exercise, suppose you guess the work TOTEM and learn that the E is still not in the right place, but the M is. How many words are left?

# 8.12.5. Exercise
# The Count of Monte Cristo is a novel by Alexandre Dumas that is considered a classic. Nevertheless, in the introduction of an English translation of the book, the writer Umberto Eco confesses that he found the book to be “one of the most badly written novels of all time”.
# In particular, he says it is “shameless in its repetition of the same adjective,” and mentions in particular the number of times “its characters either shudder or turn pale.”
# To see whether his objection is valid, let’s count the number number of lines that contain the word pale in any form, including pale, pales, paled, and paleness, as well as the related word pallor. Use a single regular expression that matches any of these words. As an additional challenge, make sure that it doesn’t match any other words, like impale – you might want to ask a virtual assistant for help.

# 9.15.2. Exercise
# Two words are anagrams if you can rearrange the letters from one to spell the other. For example, tops is an anagram of stop.
# One way to check whether two words are anagrams is to sort the letters in both words. If the lists of sorted letters are the same, the words are anagrams.
# Write a function called is_anagram that takes two strings and returns True if they are anagrams.
# Using your function and the word list, find all the anagrams of takes.

# 9.15.3. Exercise
# Python provides a built-in function called reversed that takes as an argument a sequence of elements – like a list or string – and returns a reversed object that contains the elements in reverse order.
# reversed('parrot')
# <reversed at 0x7fe3de636b60>
# If you want the reversed elements in a list, you can use the list function.
# list(reversed('parrot'))
# ['t', 'o', 'r', 'r', 'a', 'p']
# Or if you want them in a string, you can use the join method.
# ''.join(reversed('parrot'))
# 'torrap'
# So we can write a function that reverses a word like this.
# def reverse_word(word):
  # return ''.join(reversed(word))
# A palindrome is a word that is spelled the same backward and forward, like “noon” and “rotator”. Write a function called is_palindrome that takes a string argument and returns True if it is a palindrome and False otherwise.
# You can use the following loop to find all of the palindromes in the word list with at least 7 letters.
# for word in word_list:
  # if len(word) >= 7 and is_palindrome(word):
    # print(word)

# 9.15.4. Exercise
# Write a function called reverse_sentence that takes as an argument a string that contains any number of words separated by spaces. It should return a new string that contains the same words in reverse order. For example, if the argument is “Reverse this sentence”, the result should be “Sentence this reverse”.
# Hint: You can use the capitalize methods to capitalize the first word and convert the other words to lowercase.

# 9.15.5. Exercise
# Write a function called total_length that takes a list of strings and returns the total length of the strings. The total length of the words in word_list should be 902,728

"""
Using the Python language, have the function LongestWord(sen) take the sen parameter
being passed and return the largest word in the string.
If there are two or more words that are the same length, return the first word from the string with that length.
Ignore punctuation and assume sen will not be empty.

"""

import re

def LongestWord(sen = ""):
    words = re.sub('[^A-Za-z0-9]+', ' ', sen).split(" ")

    longest_word = words[0]

    for word in words:
        if len(word) > len(longest_word):
            longest_word = word
    return longest_word


# keep this function call here
print(LongestWord("I love dogs"))
"""
  Difficulty:
  Code:
"""
# input: "practice makes perfect. get perfect by practice. just practice!"
# output: {practice:3, perfect:2 ...}

# TODO: Case insensitive
# TODO: Remove punctuation (alphanum)
# Dog, dog
# Michal's dog.
# Michal Michals

def strip_nonalphanum(word):
    output = ''
    for letter in word:
        if letter.isalphanum():
            output += letter
    return output


def word_count_engine(doc):
    word_count = {}
    for word in doc.split():
        # strip (non)alphanum
        word = strip_nonalphanum(word)
        word = word.lower()
        if word in word_count:
            word_count[word] += 1
        else:
            word_count[word] = 1
    return sorted(word_count, key=word_count.get, reverse=True)

# time: O(nlgn)
# space: O(n) len(doc) = n

# n = number of words in doc
# m = number of unique words in doc

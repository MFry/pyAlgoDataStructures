"""
Given two strings, write a method to decide if one is a permutation of the other.
    Questions: What do they mean by permutation?
        Answer: I want to do know if a string is an anagram of another string
    Question: Can white space be ignored?
        Answer: No
    Question: Are upper and lower case characters unique?
        Answer: nOoO
"""


def find_anagram(str_a, str_b):
    if len(str_a) != len(str_b): # Depending on our data and how we use this function, this check may be expensive
        return False
    # Upper and Lower case are not unique
    str_a = str_a.lower()
    str_b = str_b.lower()
    for letter_a, letter_b in zip(str_a, str_b[-1::]):
        if letter_a != letter_b:
            return False
    return True


def main():
    cmp_1 = 'a'
    cmp_2 = 'a'
    print('Comparing: ', cmp_1, ',', cmp_2)
    print('Result: ', find_anagram(cmp_1, cmp_2))
    cmp_1 = 'ABc'
    cmp_2 = 'CbA'
    print('Comparing: ', cmp_1, ',', cmp_2)
    print('Result: ', find_anagram(cmp_1, cmp_2))
    cmp_1 = 'sdaFGh'
    cmp_2 = 'sdaGFh'
    print('Comparing: ', cmp_1, ',', cmp_2)
    print('Result: ', find_anagram(cmp_1,cmp_2))
    cmp_1 = '     dog'
    cmp_2 = '  God'
    print('Comparing: ', cmp_1, ',', cmp_2)
    print('Result: ', find_anagram(cmp_1, cmp_2))

if __name__ == '__main__':
    main()
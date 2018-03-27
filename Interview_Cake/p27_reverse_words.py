"""

"""
import unittest


def reverse_substring_in_place(string, start, end):
    start = start
    end -= 1
    while start < end:
        string[start], string[end] = string[end], string[start]
        start += 1
        end -= 1
    return string


def reverse_words(message):
    """
     Call reverse on the entire list
     Call reverse on word by word basis
     I assume reverse() function is in place
    :param message:
    :type message: str
    :return:
    """
    message = list(message)
    message.reverse()
    start = 0
    for i in range(len(message) + 1):
        if i == len(message) or message[i] == ' ':
            end = i
            reverse_substring_in_place(message, start, end)
            start = i + 1
    return ''.join(message)


def reverse_words_and_punctuation(message):
    """
     Call reverse on the entire list
     Call reverse on word by word basis
     I assume reverse() function is in place
    :param message:
    :type message: str
    :return:
    """
    message = list(message)
    message.reverse()
    start = 0
    # Nonexhaustive punctuation list
    punctuation_list = {'.': True,
                        ',': True,
                        '!': True,
                        ' ': True}
    for i in range(len(message) + 1):
        if i == len(message) or message[i] in punctuation_list:
            end = i
            reverse_substring_in_place(message, start, end)
            start = i + 1
    return ''.join(message)


class MyTestCases(unittest.TestCase):
    def test_reverse_words(self):
        message = 'find you will pain only go you recordings security the into if'
        self.assertEqual(reverse_words(message), 'if into the security recordings you go only pain will you find')
        message = 'Yoda am I'
        self.assertEqual(reverse_words(message), 'I am Yoda')
        message = 'I'
        self.assertEqual(reverse_words(message), 'I')
        message = '.wept Jesus'
        self.assertEqual(reverse_words_and_punctuation(message), 'Jesus wept.')

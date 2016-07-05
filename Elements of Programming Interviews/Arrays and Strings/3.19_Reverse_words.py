import unittest


def reverse_words(sentence):
    sentence = list(reversed(sentence))
    start = 0
    for i, letter in enumerate(sentence):
        if letter == ' ':
            sentence = sentence[:start] + list(reversed(sentence[start:i])) + sentence[i:]
            start = i + 1
    sentence = sentence[:start] + list(reversed(sentence[start:]))
    return ''.join(sentence)


class MyTestCase(unittest.TestCase):

    def test_reverse_words(self):
        self.assertEqual(reverse_words('I am McBeth'), 'McBeth am I')
        self.assertEqual(reverse_words('Faster am I getting'), 'getting I am Faster')
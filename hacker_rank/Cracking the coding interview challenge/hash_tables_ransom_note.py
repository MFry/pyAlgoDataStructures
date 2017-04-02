import unittest


def ransom_note(magazine, ransom):
    m, n = len(magazine), len(ransom)
    assert (m > 0 and n > 0)
    if n > m:
        return False
    magazine_histogram = {}
    for word in magazine:
        magazine_histogram[word] = 1 if word not in magazine_histogram else magazine_histogram[word] + 1
    ransom_histogram = {}
    for word in ransom:
        ransom_histogram[word] = 1 if word not in ransom_histogram else ransom_histogram[word] + 1
    for key in ransom_histogram:
        if key not in magazine_histogram or ransom_histogram[key] - magazine_histogram[key] > 0:
            return False
    return True


class MyTestCases(unittest.TestCase):
    def test_rensom_note(self):
        mag = 'give', 'me', 'one', 'grand', 'today', 'night'
        ransom = 'give', 'one', 'grand', 'today'
        self.assertTrue(ransom_note(mag, ransom))
        mag = 'avtq', 'ekpvq', 'z', 'rdvzf', 'm', 'zu', 'bof', 'pfkzl', 'ekpvq', 'pfkzl', 'bof', 'zu', 'ekpvq', 'ekpvq', 'ekpvq', 'ekpvq', 'z'
        ransom = 'm', 'z', 'z', 'avtq', 'zu', 'bof', 'pfkzl', 'pfkzl', 'pfkzl', 'rdvzf', 'rdvzf', 'avtq', 'ekpvq', 'rdvzf', 'avtq'
        self.assertFalse(ransom_note(mag, ransom))


if __name__ == '__main__':
    m, n = map(int, input().strip().split(' '))
    magazine = input().strip().split(' ')
    ransom = input().strip().split(' ')
    answer = ransom_note(magazine, ransom)
    if answer:
        print("Yes")
    else:
        print("No")

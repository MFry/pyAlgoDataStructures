import unittest


def check_valid_passphrase(passphrase):
    words_found = set()
    for word in passphrase:
        if word in words_found:
            return False
        else:
            words_found.add(word)
    return True


class MyTestCases(unittest.TestCase):
    def test_check_valid_passphrase(self):
        test_case = ['aa', 'bb', 'cc', 'dd', 'ee']
        self.assertTrue(check_valid_passphrase(test_case))
        test_case = ['aa', 'bb', 'cc', 'dd', 'aa']
        self.assertFalse(check_valid_passphrase(test_case))
        test_case = ['aa', 'bb', 'cc', 'dd', 'aaa']
        self.assertTrue(check_valid_passphrase(test_case))


if __name__ == '__main__':
    valid_pass = 0
    with open('day_4_input.txt') as reader:
        line = reader.readline()
        while line:
            line = line.split()
            if check_valid_passphrase(line):
                valid_pass += 1
            line = reader.readline()
    print(valid_pass)

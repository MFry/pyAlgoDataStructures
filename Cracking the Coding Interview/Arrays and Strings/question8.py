"""

"""


def isSubstring(string, substr):
    if substr in string:
        return True
    return False


def isRotatedSubstring(string1, string2):
    """
     Check if string2 is a substring of string1
    :param string1:
    :param string2:
    :return:
    """
    test_string = string2 + string2
    return isSubstring(test_string, string1)


def main():
    print('Test 1: ', isRotatedSubstring('waterbottle', 'erbottledwat'))


if __name__ == '__main__':
    main()

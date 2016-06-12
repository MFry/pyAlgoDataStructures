"""
Implement an algorithm to determine if a string has all unique characters. What if you cannot use additional data structures?
"""


# With data structures
def check_uniqueness(str_check):
    """
        Algorithm of O(N) time with space complexity of O(k) where k <= 26
    :param str_check:
    :return:
    """
    unique_dict = {}
    for letter in str_check:
        if letter in unique_dict:
            return False
        else:
            unique_dict[letter] = True
    return True


def check_uniqueness_no_data_struct(str_check):
    for i,letter in enumerate(str_check):
        for letter_check in str_check[i+1:]:
            if letter == letter_check:
                return False
    return True



def main():
    test = ''
    print('Checking: ', test)
    print('Result: ', check_uniqueness(test), check_uniqueness_no_data_struct(test))
    test = 'a'
    print('checking: ', test)
    print('Result: ', check_uniqueness(test), check_uniqueness_no_data_struct(test))
    test = 'asdsfdsgr'
    print('Checking: ', test)
    print('Result: ', check_uniqueness(test), check_uniqueness_no_data_struct(test))
    test = 'qwertyuiopmnbvcxz'
    print('Checking: ', test)
    print('Result: ', check_uniqueness(test), check_uniqueness_no_data_struct(test))
    test = 'kgdsfjhsgdjhe'
    print('Checking: ', test)
    print('Result: ', check_uniqueness(test), check_uniqueness_no_data_struct(test))

if __name__ == '__main__':
    main()

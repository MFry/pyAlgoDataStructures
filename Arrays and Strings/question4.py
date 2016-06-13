"""
Write a method to replace all spaces in a string with '%20'. You may assume that the string has suffcient space at the
end of the string to hold the additional characters, and that you are given the "true" length of the string.
Example:
    Input: "Mr John Smith      "
    Output: "Mr%20John%20Smith"
"""


def replace_spaces(str_mod):
    str_mod = list(str_mod)
    for i, _ in enumerate(str_mod):
        if str_mod[i] == ' ':

            def shift_right(list_shift, shift_pos):
                to_shift = list_shift[shift_pos:]
                prev = ''
                for i, _ in enumerate(to_shift):
                    prev, to_shift[i] = to_shift[i], prev
                return list_shift[:shift_pos] + to_shift
            str_mod = shift_right(str_mod, i+1)
            str_mod = shift_right(str_mod, i+1)
            str_mod[i] = '%'
            str_mod[i+1] = '2'
            str_mod[i+2] = '0'
    return ''.join(str_mod)


def main():
    test = "Mr John  "
    print('Input: ', test)
    print('Output: ', replace_spaces(test))
    test = 'Mr John Smith    '
    print('Input:', test)
    print('Output: ', replace_spaces(test))
    test = '   '
    print('Input: ', test)
    print('Output:', replace_spaces(test))

if __name__ == '__main__':
    main()

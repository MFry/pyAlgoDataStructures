"""
Implement a method of compression
"""


def basic_string_compression(to_compress):
    i = 0
    compressed = [[to_compress[0], 0]]
    while i < len(to_compress):
        char_compress = to_compress[i]
        t = compressed[-1]
        if compressed[-1][0] == char_compress:
            compressed[-1][1] += 1
        else:
            compressed.append([char_compress, 1])
        i +=1
    # construct new string
    new_str = ''
    for perm_char, count in compressed:
        new_str += perm_char +str(count)
    if len(new_str) >= len(to_compress):
        return to_compress
    else:
        return new_str


def main():
    test = 'aaa'
    print('Input: ', test)
    print('Output: ', basic_string_compression(test))
    test = 'aabcccccaaa'
    print('Input:', test)
    print('Output:', basic_string_compression(test))
    test = 'abcdefghijklmnopqrstuvwxyz'
    print('Input:', test)
    print('Output:', basic_string_compression(test))

if __name__ == '__main__':
    main()

'''                                 == EN ==
    You have a list of words. Letters of these words are mixed with extra
    symbols, so it is hard to define the beginning and end of each word. Write a
    program that will clean up the words from extra numbers and symbols.

    Input: a string with different characters. Letters are both lowercase and
    uppercase, and are mixed with extra symbols.

    Output: the cleaned up words separated by spaces in lowercase letters.
'''


def cleaner(line):
    words, word = [], ''
    for char in line:
        if char.isalpha():
            word += char
        elif word:
            words.append(word)
            word = ''
    if word:
        words.append(word)
    return ' '.join(words).lower()


if __name__ == '__main__':
    assert cleaner('(--9Hello----World...--)\n') == 'hello world', 'first'
    assert cleaner('Can 0$9 ---you~\n') == 'can you', 'second'
    assert cleaner('13What213are;11you-123+138doing7\n') == \
           'what are you doing', 'third'
    assert cleaner('Can 0$9 ---you') == 'can you', 'fourth'

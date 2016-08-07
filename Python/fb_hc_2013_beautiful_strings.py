'''                                 == EN ==
    Credits: This problem appeared in the Facebook Hacker Cup 2013 Hackathon.

    When John was a little kid he didn't have much to do. There was no internet,
    no Facebook, and no programs to hack on. So he did the only thing he
    could... he evaluated the beauty of strings in a quest to discover the most
    beautiful string in the world.

    Given a string s, little Johnny defined the beauty of the string as the sum
    of the beauty of the letters in it. The beauty of each letter is an integer
    between 1 and 26, inclusive, and no two letters have the same beauty. Johnny
    doesn't care about whether letters are uppercase or lowercase, so that
    doesn't affect the beauty of a letter. (Uppercase 'F' is exactly as
    beautiful as lowercase 'f', for example.)

    You're a student writing a report on the youth of this famous hacker. You
    found the string that Johnny considered most beautiful. What is the maximum
    possible beauty of this string?

    Input: A string.

    Output: The maximum beauty for the string.
'''


from string import ascii_lowercase
from time import time, sleep


def beauty(string):
    '''
    Define the beauty of the given string
    '''
    string = string.lower()
    quant = {letter: 0 for letter in ascii_lowercase}

    for char in string:
        if char in quant:
            quant[char] += 1

    value = sorted(quant, key=lambda i: quant[i])
    return sum(value.index(char) + 1 for char in string if char in quant)


def beauty2(string):
    '''
    Define the beauty of the given string (alternative variant)
    '''
    string = string.lower()
    letters = {}

    for char in string:
        if char in ascii_lowercase:
            if char not in letters:
                letters[char] = 0
            else:
                letters[char] += 1

    frequency = sorted(letters, key=lambda i: letters[i], reverse=True)
    values = {letter: 26 - i for i, letter in enumerate(frequency)}

    return sum(values[letter] for letter in string if letter in values)


def beauty3(string):
    '''
    Define the beauty of the given string (based on generators variant)
    '''
    string = string.lower()
    values = {letter: 26 - i for i, letter in enumerate(
                sorted(set((char for char in string if char in ascii_lowercase)),
                        key=lambda letter: string.count(letter), reverse=True))}
    return sum(values[letter] for letter in string if letter in values)


if __name__ == '__main__':
    '''
    Note: speed test results may vary. For clear results run test couple times.
    '''
    delay = 1

    start = time()
    assert beauty('ABbCcc') == 152, 'first'
    assert beauty('Good luck in the Facebook Hacker Cup this year!') == 754, 'second'
    assert beauty('Ignore punctuation, please :)') == 491, 'third'
    assert beauty('Sometimes test cases are hard to make up.') == 729, 'fourth'
    assert beauty('So I just go consult Professor Dalves') == 646, 'fifth'
    sleep(1)    # can't mesuare productivity without delay
    print('beauty()  test done in', '%.15f' % (time() - start - delay))

    start = time()
    assert beauty2('ABbCcc') == 152, 'first'
    assert beauty2('Good luck in the Facebook Hacker Cup this year!') == 754, 'second'
    assert beauty2('Ignore punctuation, please :)') == 491, 'third'
    assert beauty2('Sometimes test cases are hard to make up.') == 729, 'fourth'
    assert beauty2('So I just go consult Professor Dalves') == 646, 'fifth'
    sleep(1)    # can't mesuare productivity without delay
    print('beauty2() test done in', '%.15f' % (time() - start - delay))

    start = time()
    assert beauty3('ABbCcc') == 152, 'first'
    assert beauty3('Good luck in the Facebook Hacker Cup this year!') == 754, 'second'
    assert beauty3('Ignore punctuation, please :)') == 491, 'third'
    assert beauty3('Sometimes test cases are hard to make up.') == 729, 'fourth'
    assert beauty3('So I just go consult Professor Dalves') == 646, 'fifth'
    sleep(1)
    print('beauty3() test done in', '%.15f' % (time() - start - 1))

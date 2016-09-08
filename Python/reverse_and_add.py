'''                                 == EN ==
    The problem is as follows: choose a number, reverse it's digits and add it
    to the original. If the sum is not a palindrome (which means, it is not the
    same number from left to right and right to left), repeat this procedure.

    For example:
        195 (initial number) + 591 (reverse of initial number) = 786
        786 + 687 = 1473
        1473 + 3741 = 5214
        5214 + 4125 = 9339 (palindrome)

    In this particular case the palindrome 9339 appeared after the 4th addition.
    This method leads to palindromes in a few step for almost all of the
    integers. But there are interesting exceptions. 196 is the first number for
    which no palindrome has been found. It is not proven though, that there is
    no such a palindrome.

    Input: a string with an integer n < 10,000. Assume each test case has an
    answer if it is computable with less than 100 iterations (additions),
    otherwise return a blank string.

    Output: a string with the number of iterations (additions) to compute the
    palindrome and the resulting palindrome (they should be on one line and
    separated by a single space character) or a blank string if no palindrome
    was found.
'''


def palindrome(number):
    number = number.strip()
    for count in range(1, 101):
        number = str(int(number) + int(number[::-1]))
        length = len(number)
        # define indexes to split the number for check
        if length % 2 == 0:
            i = int(length / 2)
            sep = (i, i)
        else:
            i = int(length // 2)
            sep = (i, i + 1)
        # check if number is a palindrome
        if number[:sep[0]] == number[sep[1]:][::-1]:
            return '%d %s' % (count, number)
    return ''


if __name__ == '__main__':
    test_cases = [('195', '4 9339'),
                  ('2711', '1 3883'),
                  ('4741', '3 25652'),
                  ('1706', '1 7777'),
                  ('4291', '3 25652'),
                  ('375', '15 8836886388'),
                  ('3857', '2 15851'),
                  ('119', '2 1331'),
                  ('196', '')]
    
    for test in test_cases:
        assert palindrome(test[0]) == test[1], 'failed %s' % test[0]

'''                                 == EN ==
    Credits: This challenge appeared in the Facebook Hacker Cup 2011.

    A double-square number is an integer X which can be expressed as the sum of
    two perfect squares. For example, 10 is a double-square because
    10 = 3^2 + 1^2. Your task in this problem is, given X, determine the number
    of ways in which it can be written as the sum of two squares.

    For example, 10 can only be written as 3^2 + 1^2 (we don't count 1^2 + 3^2
    as being different). On the other hand, 25 can be written as 5^2 + 0^2 or as
    4^2 + 3^2.

    NOTE: Do NOT attempt a brute force approach. It will not work. The following
    constraints hold:
        1. 0 <= X <= 2147483647
        2. 1 <= N <= 100

    Input: a string with the value of X.

    Output: number of ways as an integer.
'''

from math import sqrt


def ds(number):
    number = int(number)
    limit = int(sqrt(number))
    ways = 0
    for x in range(limit + 1):
        y = sqrt(number - x ** 2)
        if y < x:       # further there will be only repetitions
            break       # abort the cycle to increase code speed
        if y == int(y):
            ways += 1
    return ways


if __name__ == '__main__':
    assert ds('10') == 1, 'first'
    assert ds('25') == 2, 'second'
    assert ds('3') == 0, 'third'
    assert ds('0') == 1, 'fourth'
    assert ds('1') == 1, 'fifth'
    assert ds('29641625') == 32, 'sixth'
    assert ds('801125') == 16, 'seventh'

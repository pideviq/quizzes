'''                                 == EN ==
    You are given a sorted array of positive integers and a number 'X'. Print
    out all pairs of numbers whose sum is equal to X. Print out only unique
    pairs and the pairs should be in ascending order.

    Input: a string with a comma separated list of sorted numbers and then the
    sum 'X', separated by semicolon.

    Output: a string with the pairs of numbers that are equal to the sum X. The
    pairs should themselves be printed in sorted order i.e. the first number of
    each pair should be in ascending order. If no pair exists, print the string
    'NULL'.
'''


def pairs(line):
    numbers, total = [[int(i) for i in part.split(',')]
                      for part in line.rstrip().split(';')]
    total = total[0]
    result = []
    for i, n1 in enumerate(numbers[:-1], 1):
        if n1 >= total:     # to increase code speed
            break           # (the rest sums will be greater then total)
        for n2 in numbers[i:]:
            if n1 + n2 == total:
                result.append((n1, n2))
                break       # also increases code speed
    return ';'.join('%d,%d' % pair for pair in result) if result else 'NULL'


if __name__ == '__main__':
    assert pairs('1,2,3,4,6;5\n') == '1,4;2,3', 'first'
    assert pairs('2,4,5,6,9,11,15;20\n') == '5,15;9,11', 'second'
    assert pairs('1,2,3,4;50\n') == 'NULL', 'third'
    assert pairs('5,7,13,15,20,25,30,35,40;20\n') == '5,15;7,13', 'fourth'

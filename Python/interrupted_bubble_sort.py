'''                                 == EN ==
    Bubble sort is the simplest algorithm for elements sorting. At each
    iteration we sequentially compare values of subsequent elements and swap
    them if necessary.

    Your job is to write a program which finds a state of a given list of
    positive integer numbers after applying a given count of bubble sort
    iterations.

    Input: a string which contains a space-separated list of positive integers
    and ends with a number of iterations, separated by vertical line ‘|’.

    Output: a string which contains the state of given list after applying a
    given count of bubble sort iterations (list elements are space-separated).
'''


def bubble(line):
    array, count = [[int(n) for n in group.split()]
                    for group in line.rstrip().split(' | ')]
    # there is no need to iterate more than (length_of_array - 1) times
    count = min(count[0], len(array) - 1)
    # also if the array is already sorted we should abort iterations
    is_sorted = False
    while count > 0 and not is_sorted:
        count -= 1
        is_sorted = True
        for j in range(1, len(array)):
            if array[j] < array[j - 1]:
                array[j - 1], array[j] = array[j], array[j - 1]
                is_sorted = False
    return ' '.join(str(n) for n in array)


if __name__ == '__main__':
    test_cases = [('36 47 78 28 20 79 87 16 8 45 72 69 81 66 60 8 3 86 90 90 ' \
                   '| 1\n', '36 47 28 20 78 79 16 8 45 72 69 81 66 60 8 3 86 ' \
                   '87 90 90'),
                  ('40 69 52 42 24 16 66 | 2\n', '40 42 24 16 52 66 69'),
                  ('54 46 0 34 15 48 47 53 25 18 50 5 21 76 62 48 74 1 43 74 ' \
                   '78 29 | 6\n', '0 15 25 18 34 5 21 46 47 48 48 1 43 50 53 ' \
                   '29 54 62 74 74 76 78'),
                  ('48 51 5 61 18 | 2\n', '5 48 18 51 61'),
                  ('59 68 55 31 73 4 1 25 26 19 60 0 | 2\n',
                   '55 31 59 4 1 25 26 19 60 0 68 73'),
                  ('1 2 3 | 1000000000000\n', '1 2 3')]

    for i, test in enumerate(test_cases):
        assert bubble(test[0]) == test[1], 'failed test No. %d' % i
    else:
        print('Test has been passed.')

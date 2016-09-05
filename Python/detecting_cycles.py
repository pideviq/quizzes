'''                                 == EN ==
    Given a sequence, write a program to detect cycles within it.

    Input: a string with a sequence of numbers (space delimited).

    Output: a string with the first cycle you find in each sequence. Ensure that
    there are no trailing empty spaces on each line you return.

    Constrains:
        1. The elements of the sequence are integers in range [0, 99]
        2. The length of the sequence is in range [0, 50]
'''


def first_cycle(numbers):
    numbers = numbers.rstrip().split(' ')
    result = []
    for i, n in enumerate(numbers):
        if numbers.count(n) > 1:
            repeat = i + numbers[i + 1:].index(n) + 1
            main = numbers[i:repeat]
            length = len(main)
            rest = numbers[repeat:repeat + length]
            for j in range(length):
                if main[j] == rest[j]:
                    result.append(rest[j])
                    j += 1
                else:
                    break
            break
    return ' '.join(result)


if __name__ == '__main__':
    assert first_cycle('2 0 6 3 1 6 3 1 6 3 1\n') == '6 3 1', 'first'
    assert first_cycle('3 4 8 0 11 9 7 2 5 6 10 1 49 49 49\n') == '49', 'second'
    assert first_cycle('1 2 3 1 2 3 1 2 3\n') == '1 2 3', 'third'
    assert first_cycle('5 6 10 1 16 16\n') == '16', 'fourth'

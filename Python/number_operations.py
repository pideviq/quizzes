'''                                 == EN ==
    Alice has invented a new card game to play with Bob. Alice made a deck of
    cards with random values between 1 and 52. Bob picks 5 cards. Then, he has
    to rearrange the cards so that by utilizing the operations plus, minus, or
    times, the value of the cards reach Alice's favorite number, 42. More
    precisely, find operations such that
    ((((val1 op1 val2) op2 val3) op3 val4) op4 val5) = 42.

    Help Bob by writing a program to determine whether it is possible to reach
    42 given 5 card values.

    For example, Bob picks 5 cards out of the deck containing 60, 1, 3, 5, and
    20. Bob rearranges the cards and supplies four operations, so that
    5 * 20 - 60 + 3 - 1 = 42.

    Input: a string consists of five integers, separated by spaces. Each integer
    V is 0 <= V <= 52.

    Output: a string containing "YES" if it is possible to reach the value 42
    according to the rules of the game, or "NO" otherwise.
'''


from itertools import permutations, product


OPERATORS_CHAINS = list(product('+-*', repeat=4))


def make_operation(op_type, x, y):
    return {'+': x + y,
            '-': x - y,
            '*': x * y}[op_type]


def reach_target(numbers, target=42):
    '''
    Takes the list of numbers and optional target value.

    Returns True if it is possible to reach the target using given mathematical
    operators (+, -, *), otherwise False.
    '''
    for num_seq in permutations(numbers):
        for op_seq in OPERATORS_CHAINS:
            result = make_operation(op_seq[0], num_seq[0], num_seq[1])
            result = make_operation(op_seq[1], result, num_seq[2])
            result = make_operation(op_seq[2], result, num_seq[3])
            result = make_operation(op_seq[3], result, num_seq[4])
            if result == target:
                return True
    return False


def game(cards):
    cards = [int(card) for card in cards.strip().split()]
    return 'YES' if reach_target(cards) else 'NO'


if __name__ == '__main__':
    test_cases = [('60 1 3 5 20\n', 'YES'),
                  ('44 6 1 49 47', 'NO'),
                  ('34 1 49 2 21', 'YES'),
                  ('31 38 27 51 18', 'NO')]
    for i, test in enumerate(test_cases, 1):
        assert game(test[0]) == test[1], 'failed test No.%d' % i
    else:
        print('Test has been passed.')

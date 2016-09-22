'''                                 == EN ==
    You have a pile of bricks. Every brick has it's index number and coordinates
    of opposite vertices.

    You know that somewhere on the wall there is a rectangular hole, and you are
    given coordinates of opposite vertices of that hole.

    Determine which bricks may pass through that hole.

    In situations where brick and hole have an equal sizes, we assume that it
    can pass through this hole.

    All the holes are two-dimensional. All of the bricks are three-dimensional.

    Input: a string that contains coordinates of opposite vertices of a hole
    (before the vertical bar) separated by space bar and the list of bricks you
    need to check. Each brick is enclosed in parentheses where the 1st number is
    a brick's index number, the 2nd and 3rd group of numbers are brick's
    coordinates of opposite vertices (separated by a space bar), each brick is
    divided by semicolon.

    Output: for each set of bricks produce a string with list of bricks (their
    index numbers in ascending order separated by comma) that can pass through
    the hole or "-" if none such bricks detected.
'''


def pile(line):
    hole, bricks = line.rstrip().split('|')
    hole = [[int(i) for i in point.split(',')]
            for point in hole.strip('[]').split('] [')]
    bricks = [[[int(i) for i in b.strip('[]').split(',')]
               for b in brick.split(' ')]
              for brick in bricks.strip('()').split(');(')]
    hole_size = [abs(hole[0][i] - hole[1][i]) for i in range(2)]
    # sort sizes to compare the least with the least
    hole_size.sort()
    result = []
    for brick in bricks:
        sizes = [abs(brick[1][i] - brick[2][i]) for i in range(3)]
        # we will use only two smallest values for check
        sizes.sort()
        if all(sizes[i] <= hole_size[i] for i in range(2)):
            result.append(brick[0][0])
    result.sort()
    return ','.join(str(r) for r in result) if result else '-'


if __name__ == '__main__':
    test_cases = [
            ('[4,3] [3,-3]|(1 [10,9,4] [9,4,2])\n', '1'),
            ('[-1,-5] [5,-2]|(1 [4,7,8] [2,9,0]);(2 [0,7,1] [5,9,8])\n', '1,2'),
            ('[-4,-5] [-5,-3]|(1 [4,8,6] [0,9,2]);(2 [8,-1,3] [0,5,4])\n', '-'),
            ('[6,84] [79,95]|(1 [64,86,97] [-96,70,-92]);(2 [-97,-81,-60] ' \
             '[33,-93,-80]);(3 [-16,74,-51] [-26,-54,-88]);(4 [-51,-77,32] ' \
             '[18,17,-67]);(5 [60,-2,-16] [69,-82,55]);(6 [60,-79,47] ' \
             '[-90,48,-71]);(7 [91,-43,-66] [70,-84,77]))\n', '3,5'),
            ('[0,0] [100,100]|(1 [2,3,5] [42,61,10]);(3 [5,6,6] [12,3,7]);' \
             '(2 [3,2,1] [12,6,7])\n', '1,2,3'),
    ]

    for test in test_cases:
        assert pile(test[0]) == test[1], 'failed %s' % test[0]
    else:
        print('Test has been passed.')

'''                                 == EN ==
    Sudoku is a number-based logic puzzle. It typically comprises of a 9*9 grid
    with digits so that each column, each row and each of the nine 3*3 sub-grids
    that compose the grid contains all the digits from 1 to 9. For this
    challenge, you will be given an N*N grid populated with numbers from 1
    through N and you have to determine if it is a valid sudoku solution. You
    may assume that N will be a valid number. The grid can be divided into
    square regions of equal rgn_size, where the rgn_size of a region is equal to
    the square root of a side of the entire grid. Thus for a 9*9 grid there
    would be 9 regions of rgn_size 3*3 each.

    Input: a string contains the value of N, a semicolon and the sqaure matrix
    of integers in row major form, comma delimited.

    Output: a string contains True/False if the grid is a valid sudoku layout.
'''


def validator(array, N):
    return all(d in array for d in range(1, N + 1))

# slower but less memory usage
def validator2(array, N):
    for d in range(1, N + 1):
        if d not in array:
            return False
    return True


def sudoku(line):
    N, grid = [[int(i) for i in part.split(',')] for part in line.split(';')]
    N = N[0]
    rgn_size = int(N ** .5)
    # validate input
    if N ** .5 != rgn_size or len(grid) != N ** 2:
        return 'False'
    # simplify the grid by splitting it for rows
    grid = [grid[i:i + N] for i in range(0, N ** 2, N)]
    # uncomment the line below to print out the grid
    # for r in grid: print(r)

    # validate rows
    rows = all(validator(row, N) for row in grid)
    if rows:
        # validate columns
        cols = all(validator([row[i] for row in grid], N) for i in range(N))
        if cols:
            # validate regions
            for rgn_line in range(0, N, rgn_size):
                rgn_line = grid[rgn_line:rgn_line + rgn_size]
                for rgn_col in range(0, N, rgn_size):
                    region = [r[j] for r in rgn_line
                              for j in range(rgn_col, rgn_col + rgn_size)]
                    if not validator(region, N):
                        return 'False'
    return 'True' if rows and cols else 'False'


if __name__ == '__main__':
    test_cases = [('4;1,4,2,3,2,3,1,4,4,2,3,1,3,1,4,2\n', 'True'),
                  ('4;2,1,3,2,3,2,1,4,1,4,2,3,2,3,4,1\n', 'False'),
                  ('9;1,2,7,5,3,9,8,4,6,4,5,3,8,6,1,7,9,2,8,9,6,4,7,2,1,5,3,2' \
                   ',8,9,3,1,7,4,6,5,3,6,5,2,8,4,9,1,7,7,4,1,9,5,6,3,2,8,9,7,' \
                   '4,6,2,8,5,3,1,5,1,2,7,4,3,6,8,9,6,3,8,1,9,5,2,7,4', 'True'),
                  ('9;8,7,1,4,6,9,3,5,2,4,2,6,3,5,1,8,9,7,5,9,3,7,2,8,4,6,1,3' \
                   ',5,2,9,4,7,6,1,8,6,4,9,1,8,2,5,7,3,1,8,7,5,3,6,2,4,9,9,6,' \
                   '4,2,1,3,7,8,5,7,3,8,6,9,5,1,2,4,2,1,5,8,7,4,9,3,6', 'True'),
                  ('9;1,9,8,5,2,3,7,4,5,2,9,1,7,4,6,3,3,9,4,5,9,2,8,7,2,9,9,4' \
                   ',7,8,2,5,4,5,6,2,3,4,9,4,4,3,5,5,5,6,5,4,3,2,2,1,8,1,5,3,' \
                   '9,4,7,8,2,3,5,6,5,6,4,1,7,7,6,4,3,3,1,1,1,9,3,8,7', 'False'),
                  ('5;1,4,2,3,2,3,1,4,4,2,3,1,3,1,4,2\n', 'False'),
                  ('4;1,4,2,3,2,3,1,4,4,2,3,1,3,1,4,2,1\n', 'False')]

    for test in test_cases:
        assert sudoku(test[0]) == test[1], 'failed %s' % test[0]
    else:
        print('Test has been passed.')

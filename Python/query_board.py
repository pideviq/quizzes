'''                                 == EN ==
    There is a board (matrix). Every cell of the board contains one integer,
    which is 0 initially.

    The next operations can be applied to the Query Board:
    SetRow i x: it means that all values in the cells on row "i" have been
                changed to value "x" after this operation.
    SetCol j x: it means that all values in the cells on column "j" have been
                changed to value "x" after this operation.
    QueryRow i: it means that you should output the sum of values on row "i".
    QueryCol j: it means that you should output the sum of values on column "j".

    Conditions:
    The board's dimensions are 256x256
    "i" and "j" are integers from 0 to 255
    "x" is an integer from 0 to 31

    Input: A list of operations.

    Output: A list of answers of the queries.
'''


class QueryBoard:
    '''
    Simple database that support queries
    '''
    def __init__(self):
        self.matrix = [[0 for col in range(256)] for row in range(256)]

    def set_row(self, row, value):
        '''
        Change values of all cells in row "row" to "value"
        '''
        self.matrix[row] = [value for col in range(256)]

    def set_col(self, col, value):
        '''
        Change values of all cells in column "col" to "value"
        '''
        for row in range(len(self.matrix)):
            self.matrix[row][col] = value

    def query_row(self, row):
        '''
        Define the sum of values in row "row"
        '''
        return sum(self.matrix[row])

    def query_col(self, col):
        '''
        Define the sum of values in column "col"
        '''
        return sum(self.matrix[row][col] for row in range(len(self.matrix)))



def query(commands):
    qb = QueryBoard()
    answer = []

    for command in commands:
        operation = command.strip().split(' ')
        if operation[0] == 'SetCol':
            qb.set_col(int(operation[1]), int(operation[2]))
        elif operation[0] == 'SetRow':
            qb.set_row(int(operation[1]), int(operation[2]))
        elif operation[0] == 'QueryCol':
            answer.append(qb.query_col(int(operation[1])))
        elif operation[0] == 'QueryRow':
            answer.append(qb.query_row(int(operation[1])))

    return answer


if __name__ == '__main__':
    commands = [
        'SetCol 32 20\n',
        'SetRow 15 7\n',
        'SetRow 16 31\n',
        'QueryCol 32\n',
        'SetCol 2 14\n',
        'QueryRow 10\n',
        'SetCol 14 0\n',
        'QueryRow 15\n',
        'SetRow 10 1\n',
        'QueryCol 2\n',
    ]
    answer = [5118, 34, 1792, 3571]

    assert query(commands) == answer, 'Wrong answer: ' + answer

'''                                 == EN ==
    Have you ever tried to win in the 2048 game? In this challenge, your task is
    to implement part of the logic of this game.

    The original 2048 is played on a 4×4 grid, with numbered tiles that slide
    when a player moves them using the four arrow keys. Tiles slide as far as
    possible in the chosen direction until they are stopped by either another
    tile or the edge of the grid. If two tiles of the same number collide while
    moving, they will merge into a tile with the total value of the two tiles
    that collided. The resulting tile cannot merge with another tile again in
    the same move. (To try this game in action visit it's official site:
    https://gabrielecirulli.github.io/2048/)

    In this challenge, you have to implement the logic for the sliding tiles in
    the chosen direction. Unlike the original game, a new tile cannot appear
    after the move and the grid size may vary from 4 to 10.

    Input: a string that consists of a direction (UP, DOWN, RIGHT, or LEFT), the
    length of a side in the square grid, and the initial configuration of the
    grid. All the data elements are separated by a semicolon. The configuration
    of the grid is a series of lines from top to bottom separated by a vertical
    bar. 0 indicates a blank tile.

    Output: a string with the configuration of the grid received after slide of
    a tile in the chosen direction. Format is the same as in the input file.
    Lines are written from top to bottom and are separated by a vertical bar.
    Blank tiles are marked with 0.

    Constraints:
        1. The grid is square with the length of a side from 4 to 10.
        2. The value of the tiles is equal to the power of number 2 and varies
        from 2^1 to 2^10.
'''


def game(line):
    move, dimension, grid = line.strip().split(';')
    grid = [[int(tile) for tile in row.strip().split()]
            for row in grid.split('|')]
    dimension = int(dimension)
    new_grid = []

    if move in ('UP', 'DOWN'):
        # rotate the grid clockwise by 90 degrees
        # to use in all-purpose algorithm
        grid = [[grid[i][j] for i in range(dimension - 1, -1, -1)]
                for j in range(dimension)]

    for row in grid:
        buffer = []
        if move in ('UP', 'RIGHT'):
            # reverse the row for the all-purpose algorithm
            row = row[::-1]
        for tile in row:
            if tile:
                if buffer and not buffer[-1][1] and buffer[-1][0] == tile:
                    buffer[-1] = (tile * 2, True)
                else:
                    # all tiles looks like: (value, merging_flag)
                    buffer.append((tile, False))
        new_row = [tile[0] for i, tile in enumerate(buffer)]
        if len(new_row) < dimension:
            # extend row by zero(s) (empty tiles)
            new_row += [0] * (dimension - len(new_row))
        if move in ('UP', 'RIGHT'):
            # reverse again to get correct order
            new_row = new_row[::-1]
        new_grid.append(new_row)

    if move in ('UP', 'DOWN'):
        # rotate the grid counterclockwise by 90 degrees
        # to get initial-like grid
        new_grid = [[new_grid[i][j] for i in range(dimension)]
                    for j in range(dimension - 1, -1, -1)]

    return '|'.join(' '.join(str(tile) for tile in row)
                    for row in new_grid)


if __name__ == '__main__':
    test_cases = [('RIGHT; 4; 4 0 2 0|0 0 0 8|4 0 2 4|2 4 2 2',
                   '0 0 4 2|0 0 0 8|0 4 2 4|0 2 4 4'),
                  ('UP; 4; 2 0 2 0|0 2 0 4|2 8 0 8|0 8 0 16',
                   '4 2 2 4|0 16 0 8|0 0 0 16|0 0 0 0'),
                  ('LEFT; 4; 4 2 0 0|2 4 2 2|2 16 4 2|4 32 8 0',
                   '4 2 0 0|2 4 4 0|2 16 4 2|4 32 8 0'),
                  ('DOWN; 4; 4 2 0 0|2 4 2 2|2 16 4 2|4 32 8 0',
                   '0 2 0 0|4 4 2 0|4 16 4 0|4 32 8 4')]
    for i, test in enumerate(test_cases, 1):
        assert game(test[0]) == test[1], 'failed test No.%d' % i
    else:
        print('Test has been passed.')

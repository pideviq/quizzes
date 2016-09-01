'''                                 == EN ==
    You must have heard about pirates, their customs, pirates code, and the
    “black spot”. If a pirate is presented with a “black spot”, he is officially
    pronounced guilty, meaning he will soon be expulsed from the pirate
    brotherhood or even be dead.

    We don’t have as strict rules as pirates have, and a person who receives a
    black spot simply leaves the game.

    For example, we have a list of three players: John, Tom, Mary, and a number
    5. Starting with the first player (in our case, it’s John), we start to
    count all players: John – 1, Tom – 2, Mary – 3, and then again starting from
    the first one John – 4, Tom – 5. As Tom gets number 5, he should leave. Now,
    we have John and Mary and start counting again. John gets number 5, so he
    leaves. Thus, the winner is Mary.

    Input: a string with names of players and a number for a “black spot”.
    Players and a number are separated by a pipeline '|'.

    Output: a string with the name of a winner.

    CONSTRAINTS:
        1. Always start counting from the first name in a list.
        2. Number of players can be from 3 to 10.
        3. Number of turns can be from 3 to 15.
'''


def black(line):
    players, bs = line.rstrip().split(' | ')
    players = players.split(' ')
    bs = int(bs) - 1
    for turn in range(len(players) - 1):
        del players[bs % len(players)]
    return players[0]


if __name__ == '__main__':
    assert black('John Sara Tom Susan | 3\n') == 'Sara', 'first'
    assert black('John Tom Mary | 5\n') == 'Mary', 'second'

'''                                 == EN ==
    You are given a text. Write a program which outputs its lines according to
    the following rules:
        1. If line length is ≤ 55 characters, print it without any changes.
        2. If the line length is > 55 characters, change it as follows:
        3. Trim the line to 40 characters.
        4. If there are spaces ‘ ’ in the resulting string, trim it once again
            to the last space (the space should be trimmed too).
        5. Add a string ‘... <Read More>’ to the end of the resulting string and
            print it.

    Input: A string with text.

    Output: A string with it's length limited according to the rules described
            above.

    CONSTRAINTS:
        1. The maximum length of a line in the input file is 300 characters.
        2. There cannot be more than one consequent space character in the input
            data.
'''


def trimmer(line):
    line = line.strip()

    if len(line) <= 55:
        return line
    else:
        line = line.split(' ')
        result, limit = [], 40

        if len(line[0]) >= limit:
            return line[0][:limit] + '... <Read More>'

        for word in line:
            limit -= len(word)
            if limit > 0:
                result.append(word)
            else:
                break
            limit -= 1      # count space
        return ' '.join(result) + '... <Read More>'


if __name__ == '__main__':
    assert trimmer('Tom exhibited.\n') == 'Tom exhibited.', 'first'
    assert trimmer('Amy Lawrence was proud and glad, and she tried to make ' \
                   'Tom see it in her face - but he wouldn\'t look.\n') == \
           'Amy Lawrence was proud and glad, and... <Read More>', 'second'
    assert trimmer('Tom was tugging at a button-hole and looking sheepish.\n') \
           == 'Tom was tugging at a button-hole and looking sheepish.', 'third'
    assert trimmer('Two thousand verses is a great many - very, very great ' \
                   'many.\n') == \
           'Two thousand verses is a great many -... <Read More>', 'fourth'
    assert trimmer('Tom\'s mouth watered for the apple, but he stuck to his '\
                   'work.\n') == \
           'Tom\'s mouth watered for the apple, but... <Read More>', 'fifth'
    assert trimmer('123456789A123456789B123456789C123456789D123456789E123456') \
           == '123456789A123456789B123456789C123456789D... <Read More>', 'sixth'
    assert trimmer('123456789A123456789B123456789C123456789 123456789E1234 6') \
           == '123456789A123456789B123456789C123456789... <Read More>', \
           'seventh'

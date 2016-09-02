'''                                 == EN ==
    People around the world watch football matches and root for different
    football teams. Some people are fans of Real Madrid, some like Barcelona,
    some pull for Atletico Madrid, while others do not miss a single match with
    FC Bayern Munich.

    The teams would like to know people in which countries cheer for them. So,
    let’s help them!

    Input: a string with lists of countries. Lists are separated by pipelines
    '|'. Each list includes football teams that people in these countries root
    for.

    Output: for each football team, print a string with a list of countries
    where people root for them. Separate each team by a semicolon ';' and a
    space. All output should be sorted.

    CONSTRAINTS:
        1. The number of countries lists can be from 3 to 20.
        2. Each list contains a different number of football teams: from 1 to 7.
'''


# based on generators method
def fb(line):
    line = [[int(team) for team in country.split(' ')]
            for country in line.rstrip().split(' | ')]
    teams = {team for country in line for team in country}
    fans = {team: [i + 1 for i in range(len(line)) if team in line[i]]
            for team in teams}
    result = ['%d:%s;' % (team, ','.join(str(i) for i in fans[team]))
              for team in sorted(fans)]
    return ' '.join(result)


# manual method with less memory usage
def fb2(line):
    line = [country.split(' ') for country in line.rstrip().split(' | ')]
    fans = {}
    for i, country in enumerate(line, 1):
        for team in country:
            if team in fans:
                fans[team].append(str(i))
            else:
                fans[team] = [str(i)]
    result = []
    for team in sorted(fans, key=int):
        result.append('%s:%s;' % (team, ','.join(fans[team])))
    return ' '.join(result)


if __name__ == '__main__':
    assert fb('1 2 3 4 | 3 1 | 4 1\n') == '1:1,2,3; 2:1; 3:1,2; 4:1,3;', 'first'
    assert fb('19 11 | 19 21 23 | 31 39 29\n') == \
           '11:1; 19:1,2; 21:2; 23:2; 29:3; 31:3; 39:3;', 'second'

    assert fb2('1 2 3 4 | 3 1 | 4 1\n') == '1:1,2,3; 2:1; 3:1,2; 4:1,3;', 'first'
    assert fb2('19 11 | 19 21 23 | 31 39 29\n') == \
           '11:1; 19:1,2; 21:2; 23:2; 29:3; 31:3; 39:3;', 'second'

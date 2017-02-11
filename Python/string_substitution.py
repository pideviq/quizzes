'''                                 == EN ==
    Credits: This challenge was contributed by Sam McCoy.

    Given a string S, and a list of strings of positive length,
    F1,R1,F2,R2,...,FN,RN, proceed to find in order the occurrences
    (left-to-right) of Fi in S and replace them with Ri. All strings are over
    alphabet { 0, 1 }. Searching should consider only contiguous pieces of S
    that have not been subject to replacements on prior iterations. An iteration
    of the algorithm should not write over any previous replacement by the
    algorithm.

    Input: text that contains a string, then a semicolon and then a list of
    comma separated strings.

    Output: the string after substitutions have been made.

    P.S. For the curious, here are the transitions for the test example:
    10011011001 => 10100111001 [replacing 0110 with 1001] =>
    10100110 [replacing 1001 with 0] => 11100110 [replacing 10 with 11].
    So the answer is 11100110
'''


def main(data):
    string, replacements = data.rstrip().split(';')
    replacements = replacements.split(',')
    indexes = [False for i in range(len(string))]
    for i in range(0, len(replacements), 2):
        pos = 0
        while True:
            gotit = string.find(replacements[i], pos)
            rng = gotit + len(replacements[i])
            if gotit >= 0:
                if not any(indexes[gotit : rng]):
                    string = string[:gotit] + replacements[i + 1] + string[rng:]
                    indexes[gotit : rng] = [True for p in
                                            range(len(replacements[i + 1]))]
                pos += 1
            else:
                break
    return string


if __name__ == '__main__':
    assert main('10011011001;0110,1001,1001,0,10,11\n') == '11100110', 'failed'

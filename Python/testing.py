'''                                 == EN ==
    In many teams, there is a person who tests a project, finds bugs and errors,
    and prioritizes them.

    Now, you have the unique opportunity to try yourself as a tester and test a
    product. Here, you have two strings - the first one is provided by
    developers, and the second one is mentioned in design. You have to find and
    count the number of bugs, and also prioritize them for fixing using the
    following statuses: 'Low', 'Medium', 'High', 'Critical' or 'Done'.

    Write a program that counts the number of bugs and prioritizes them for
    fixing using the following statuses:
        'Low' - 2 or fewer bugs;
        'Medium' - 4 or fewer bugs;
        'High' - 6 or fewer bugs;
        'Critical' - more than 6 bugs;
        'Done' - all is done.

    Input: a string that includes a test case with two strings separated by a
    pipeline '|'. The first string is the one the developers provided to you for
    testing, and the second one is from design.

    Output: a string with status.

    CONSTRAINTS:
        1. Strings are of the same length from 5 to 40 characters.
        2. Upper and lower case matters.
'''


def test(line):
    dev, design = line.rstrip().split(' | ')
    len_dev, len_design = len(dev), len(design)
    shortest = dev if len_dev <= len_design else design
    longest = design if shortest == dev else dev
    # initialize bugs with the difference in test cases' length
    bugs = abs(len_dev - len_design)

    for i, char in enumerate(shortest):
        if char != longest[i]:
            bugs += 1

    if bugs > 4:
        if bugs > 6:
            status = 'Critical'
        else:
            status = 'High'
    else:
        if bugs > 2:
            status = 'Medium'
        elif bugs > 0:
            status = 'Low'
        else:
            status = 'Done'
    return status


if __name__ == '__main__':
    assert test('Heelo Codevval | Hello Codeeval\n') == 'Low', 'first'
    assert test('hELLO cODEEVAL | Hello Codeeval\n') == 'Critical', 'second'
    assert test('Hello Codeeval | Hello Codeeval\n') == 'Done', 'third'
    assert test('c j XrWUehjkJiPEQIwyk MlO | lyQ EJiMkXwrUjeWcIkPh jO\n') == \
           'Critical', 'fourth'

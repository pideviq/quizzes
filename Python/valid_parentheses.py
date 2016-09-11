'''                                 == EN ==
    Given a string comprising just of the characters (,),{,},[,] determine if it
    is well-formed or not.

    Input: a string comprising of the characters mentioned above.

    Output: 'True' or 'False' if the string is well-formed.
'''


brackets = {'(': ')', '[': ']', '{': '}'}


def validator(line):
    stack = []
    for char in line.rstrip():
        if char in brackets:
            stack.append(brackets[char])
        elif stack and char == stack[-1]:
            stack.pop(-1)
        else:
            return 'False'
    return 'True' if not stack else 'False'


if __name__ == '__main__':
    test_cases = [('()\n', 'True'),
                  ('([)]\n', 'False'),
                  ('([{}()][])\n', 'True'),
                  ('([{]}())\n', 'False'),
                  ('{}((\n', 'False')]

    for test in test_cases:
        assert validator(test[0]) == test[1], 'failed %s' % test[0]
    else:
        print('Test has been passed.')

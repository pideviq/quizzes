'''                                 == EN ==
    To check whether a bank card number is valid or it is just a set of random
    numbers, Luhn formula is used. The formula verifies a number against its
    included check digit, which is usually appended to a partial account number
    to generate the full account number. This account number must pass the
    following test:
        1. From the rightmost digit, which is the check digit, moving left,
        double the value of every second digit; if the product of this doubling
        operation is greater than 9 (for example, 7×2=14), then sum the digits
        of the products (for example, 12:1+2=3, 14:1+4=5).
        2. Take the sum of all the digits.
        3. If the total modulo 10 is equal to 0 (if the total ends in zero)
        then, according to the Luhn formula, the number is valid; otherwise, it
        is not valid.

    Examples of formula calculation and result checking:

    Checking number 1556 9144 6285 339
    1   5   5   6   9   1   4   4   6   2   8   5   3   3   9
    1   10  5   12  9   2   4   8   6   4   8   10  3   6   9
    1 + 1 + 5 + 3 + 9 + 2 + 4 + 8 + 6 + 4 + 8 + 1 + 3 + 6 + 9 = 70
    70 mod 10 = 0, card number is valid

    Checking number 6363 1811 2857 7650
    6   3   6   3   1   8   1   1   2   8   5   7   7   6   5   0
    12  3   12  3   2   8   2   1   4   8   10  7   14  6   10  0
    3 + 3 + 3 + 3 + 2 + 8 + 2 + 1 + 4 + 8 + 1 + 7 + 5 + 6 + 1 + 0 = 57
    57 mod 10 = 7 <> 0, card number is not valid

    Input: a string with a bank card number. For better readability, numbers are
    split into groups of 4 digits separated by spaces.

    Output: a string with the results of bank card number validation. If the
    number is correct – return "1", otherwise – "0".

    Constraints:
        1. Bank card numbers can be from 12 to 19 digits length.
        2. Numbers are split into groups of 4 digits separated by spaces,
        spaces should be ignored.
'''


def __double_number(number):
    ''' Function for internal use only '''
    number = number * 2
    if number > 9:
        return sum(int(digit) for digit in str(number))
    return number


def double_number(number):
    ''' Double the given number and return the sum of its digits '''
    try:
        number = int(number)
    except:
        print('Invalid input. Number is required.')
        return None
    return __double_number(number)


def validator(cc):
    original_cc = str(cc).strip()
    cc = original_cc.replace(' ', '')[::-1]
    # verify that card number consists only of numbers and has the right length
    if not cc.isdigit():
        print(original_cc, 'Card number must contain only digits and spaces.')
        return '0'
    if len(cc) not in range(12, 20):
        print(original_cc,
              '- Bank card number must be from 12 to 19 digits length.')
        return '0'
    checksum = sum(int(digit) if i % 2 == 0 else __double_number(int(digit))
                   for i, digit in enumerate(cc))
    return '%d' % (checksum % 10 == 0)


if __name__ == '__main__':
    test_cases = [('1556 9144 6285 339', '1'),
                  ('6363 1811 2857 7650', '0'),
                  ('6011 5940 0319 9511', '0'),
                  ('5537 0213 6797 6815', '1'),
                  ('5574 8363 8022 9735', '0'),
                  ('3044 8507 9391 30', '0'),
                  ('6370 1675 9034 6211 774', '1'),
                  ('6370 1675 9034 6211 7745', '0')]

    for i, (test, answer) in enumerate(test_cases):
        assert validator(test) == answer, 'failed test No.%d' % i
    else:
        print('Test has been passed.')

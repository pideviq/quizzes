'''                                 == EN ==
    The goal of this challenge is to design a cash register program. You will be
    given two float numbers. The first is the purchase price (PP) of the item.
    The second is the cash (CH) given by the customer. Your register currently
    has the following bills/coins within it:

        'PENNY': .01,
        'NICKEL': .05,
        'DIME': .10,
        'QUARTER': .25,
        'HALF DOLLAR': .50,
        'ONE': 1.00,
        'TWO': 2.00,
        'FIVE': 5.00,
        'TEN': 10.00,
        'TWENTY': 20.00,
        'FIFTY': 50.00,
        'ONE HUNDRED': 100.00

    The aim of the program is to calculate the change that has to be returned to
    the customer.

    Input: a string with two numbers which are separated by a semicolon. The
    first is the Purchase price (PP) and the second is the cash(CH) given by the
    customer.

    Output: a string with the change to be returned to the customer. In case the
    CH < PP, return 'ERROR'. If CH == PP, return 'ZERO'. For all other cases
    retrun the amount that needs to be returned, in terms of the currency values
    provided. The output should be sorted in highest-to-lowest order
    (DIME,NICKEL,PENNY).
'''


MONEY = [('ONE HUNDRED', 100),
         ('FIFTY', 50),
         ('TWENTY', 20),
         ('TEN', 10),
         ('FIVE', 5),
         ('TWO', 2),
         ('ONE', 1),
         ('HALF DOLLAR', .5),
         ('QUARTER', .25),
         ('DIME', .1),
         ('NICKEL', .05),
         ('PENNY', .01)]


def cash(line):
    pp, ch = [float(n) for n in line.rstrip().split(';')]
    if ch <= pp:
        if ch < pp:
            return 'ERROR'
        else:
            return 'ZERO'

    change = ch - pp
    result = []
    for m in MONEY:
        while round(change, 2) // m[1] > 0:
            result.append(m[0])
            change -= m[1]
    return ','.join(result)


if __name__ == '__main__':
    test_cases = [('15.94;16.00\n', 'NICKEL,PENNY'),
                  ('17;16\n', 'ERROR'),
                  ('35;35\n', 'ZERO'),
                  ('45;50\n', 'FIVE'),
                  ('37.22;40\n', 'TWO,HALF DOLLAR,QUARTER,PENNY,PENNY,PENNY')]

    for test in test_cases:
        assert cash(test[0]) == test[1], 'failed %s' % test[0]

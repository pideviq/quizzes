'''                                 == EN ==
    You are building a new social platform and want to store user's work
    experience. You have decided to calculate the total experience of each user
    in years based on the time periods that they provided. Using this approach,
    you need to be sure that you are taking into account the overlapping time
    periods in order to retrieve the actual work experience in years.

    For example:
        Jan 2010-Dec 2010
        Jan 2010-Dec 2010
    Two jobs with 12 months of experience each, but actual work experience is 1
    year because of the overlapping time periods. The task is to calculate the
    actual work experience based on the list of time intervals.

    Input: List of strings. Each string contains a list of time periods
    separated by a semicolon and a single space. Each time period is represented
    as the begin date and the end date. Each date consists of a month as an
    abbreviated name and a year with century as a decimal number separated by a
    single space. The begin date and the end date are separated by a hyphen.

    Output: List of actual work experience in years (integer) for each test
    case.

    CONSTRAINTS:
    The number of lines in a file is in a range from 20 to 40.
    The dates are in a range from Jan 1990 to Dec 2020.
    The end date is greater than the begin date.
    The begin date is the first day of a given month, and the end date is the
        last day of a given month.
'''

from math import floor


def experience(data):
    MN = ['%s %d' % (m, y) for y in range(1990, 2021) for m in
          ('Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun',
           'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec')]
    results = []

    for line in data:
        xp = set()
        jobs = [job.split('-') for job in line.strip().split('; ')]

        # store all working months
        for job in jobs:
            xp.update(MN[MN.index(job[0]):MN.index(job[1]) + 1])
        # save only full years
        results.append(floor(len(xp) / 12))

    return results


def experience2(data):
    '''
    Based on counting method
    '''
    MONTHS = {'Jan': 1, 'Feb': 2, 'Mar': 3, 'Apr': 4, 'May': 5, 'Jun': 6,
              'Jul': 7, 'Aug': 8, 'Sep': 9, 'Oct': 10, 'Nov': 11, 'Dec': 12}
    results = []

    for line in data:
        xp = set()
        jobs = [job.split('-') for job in line.strip().split('; ')]

        for job in jobs:
            points = (j.split(' ') for j in job)
            # count the number (id) of the month
            begin, end = (MONTHS[point[0]] + int(point[1]) * 12
                          for point in points)
            xp.update({i for i in range(begin, end + 1)})

        results.append(floor(len(xp) / 12))

    return results


if __name__ == '__main__':
    test_cases = [
        'Feb 2004-Dec 2009; Sep 2004-Jul 2008\n',
        'Aug 2013-Mar 2014; Apr 2013-Aug 2013; Jun 2014-Aug 2015; Apr 2003-'\
            'Nov 2004; Apr 2014-Jan 2015\n',
        'Mar 2003-Jul 2003; Nov 2003-Jan 2004; Apr 1999-Nov 1999\n',
        'Apr 1992-Dec 1993; Feb 1996-Sep 1997; Jan 2002-Jun 2002; Sep 2003-'\
            'Apr 2004; Feb 2010-Nov 2011\n',
        'Feb 2004-May 2004; Jun 2004-Jul 2004\n',
    ]
    answers = [5, 4, 1, 6, 0]

    assert experience(test_cases) == answers, 'experience failed'
    assert experience2(test_cases) == answers, 'experience2 failed'

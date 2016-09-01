'''                                 == EN ==
    It's amazing how fast time flies by and we don’t even realize it. As we are
    getting older, time seems to move so much faster than it did in the past.

    Perception of time is relative to how fast our heart rate is. An unborn
    baby’s heart rate is incredibly fast and as we age, it slows. Metabolic rate
    of an organism determines its perception of time. Organisms like cats and
    dogs have a very high metabolic rate; thus, the breaks between their meals
    seem to be shorter than humans have.

    At codeeval.com, we have a cat called Kitty. She loves eating, and it seems
    like she can eat anything any time. We want to keep Kitty fit, so we feed
    her according to a schedule.

    Planning her daily meals, we need to see when Kitty will eat starting with
    the latest meal in the evening to the earliest morning snack. So, your task
    is to sort timestamps in the schedule in a reverse chronological order.

    Input: a string with a schedule containing unsorted timestamps in
    HH:MM:SS format.

    Output: a string with a schedule containing sorted timestamps (from the
    biggest to the smallest one).

    CONSTRAINTS:
        1. Each schedule may have from 2 to 20 timestamps.
        2. Timestamp 23:59:59 - biggest and 00:00:01 the smallest one.
'''

# based on using datetime.time method (huge memory usage)
from datetime import time

def schedule(times):
    times = [[int(i) for i in t.split(':')] for t in times.rstrip().split(' ')]
    times = [time(t[0], t[1], t[2]) for t in times]
    times.sort(reverse=True)
    times = ['%02d:%02d:%02d' % (t.hour, t.minute, t.second) for t in times]
    return ' '.join(times)


# based on manual conversion method (speed is equal to the first method, but
#   much less memory usage)
def schedule2(times):
    times = [[int(i) for i in t.split(':')] for t in times.rstrip().split(' ')]
    times = [t[0] * 3600 + t[1] * 60 + t[2] for t in times]
    times.sort(reverse=True)
    result = []
    for t in times:
        h = t // 3600
        t = t % 3600
        m = t // 60
        t = t % 60
        result.append('%02d:%02d:%02d' % (h, m, t))
    return ' '.join(result)


# optimised method with manual conversions (the best speed and memory usage)
def schedule3(times):
    times = times.rstrip().split(' ')
    times.sort(key=lambda x: sum(int(t) * (60 ** i) for i, t in
                                 enumerate(x.split(':')[::-1])), reverse=True)
    return ' '.join(times)


if __name__ == '__main__':
    assert schedule('02:26:31 14:44:45 09:53:27\n') == \
           '14:44:45 09:53:27 02:26:31', 'first'
    assert schedule('05:33:44 21:25:41\n') == '21:25:41 05:33:44', 'second'

    assert schedule2('02:26:31 14:44:45 09:53:27\n') == \
           '14:44:45 09:53:27 02:26:31', 'first'
    assert schedule2('05:33:44 21:25:41\n') == '21:25:41 05:33:44', 'second'

    assert schedule3('02:26:31 14:44:45 09:53:27\n') == \
           '14:44:45 09:53:27 02:26:31', 'first'
    assert schedule3('05:33:44 21:25:41\n') == '21:25:41 05:33:44', 'second'

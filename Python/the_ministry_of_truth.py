'''                                 == EN ==
    It's 1984, and you are working as an official at the Ministry of Truth. You
    have intersected a message subjected to Big Brother's doctrine.

    Your task is to delete letters from certain "utterances" in order to replace
    them with an "utterance" approved by the Ministry.

    A "word" is a single sequence of Latin letters, and an "utterance" is a
    sequence of multiple words and spaces.

    To compare two "utterances," you have to replace all blocks of spaces with
    one space. Utterances are considered to be identical when resulting
    expressions match.

    One line contains two different expressions separated by semicolon ';'. The
    first expression is the original utterance, and the second one is the
    utterance you want to get.

    If you cannot fulfill the order, print a single line "I cannot fix history".
    Otherwise, output the original utterance by replacing the letters that must
    be erased with underscore and by replacing all blocks of white spaces with a
    single white space.

    Input: a string with original and "approved" utterances separated by
    semicolon ';'

    Output: a string with the results, or "I cannot fix history" in case there
    is no match.
'''


def censor(line):
    original, approved = [s.split() for s in line.rstrip().split(';')]
    # if it's allowed nothing to print
    if not approved:
        final = ['_' * len(word) for word in original]
        return ' '.join(final)

    final = []
    for word in original:
        index = word.find(approved[0]) if approved else -1
        if index > -1:
            final.append('_' * len(word[:index]) + approved[0] +
                         '_' * len(word[index + len(approved[0]):]))
            approved.pop(0)
        else:
            final.append('_' * len(word))
    return ' '.join(final) if not approved else 'I cannot fix history'


if __name__ == '__main__':
    test_cases = [('Higher meaning;Hi mean\n', 'Hi____ mean___'),
                  ('this is impossible;im possible\n', 'I cannot fix history'),
                  ('twenty   two minutes;two minutes\n', '______ two minutes'),
                  ('Higher meaning;e\n', '____e_ _______'),
                  ('DfH   SpOVbdGkGOP eCNz  nfxsrnnsuEa;S srnns',
                   '___ S__________ ____ ___srnns___'),
                  ('gxoDV  RqRshDNgW tkLVWqU   NbWfeYTkVavgb yavZ;NgW eYTkVavg',
                   '_____ ______NgW _______ ____eYTkVavg_ ____'),
                  ('ffa   fj;', '___ __'),
                  ('ya Preved to Medved;Preved ed', '__ Preved __ _ed___'),
                  ('bjc degb jehc;tqll', 'I cannot fix history'),
                  ('bjc degb jehc;je bj', 'I cannot fix history'),
                  ('The string with wrong order;ron ring',
                   'I cannot fix history')]

    for i, test in enumerate(test_cases):
        assert censor(test[0]) == test[1], 'failed test No. %d' % i
    else:
        print('Test has been passed.')

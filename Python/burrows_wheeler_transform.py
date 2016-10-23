'''                                 == EN ==
    You are trying to unpack a text compressed using run-length encoding. You
    are doing everything right, but get absolutely ridiculous results. As it
    came out, before the compression, somebody used the Burrows-Wheeler
    algorithm. It allows increasing the number of repeated characters in the
    text, and thus, increase the efficiency of compression. This method is used
    by the bzip2 utility.

    Let’s examine the line processing using the Burrows-Wheeler algorithm. First
    of all, we should mark the end of the line with a special character (EOF),
    it is $ in this case. Then, generate all possible rotations of the line,
    sort them alphabetically and construct a new string — Burrows-Wheeler
    transform  — from the last characters of each rotation.

    For example, the line ‘easy-peasy’ is transformed as follows:

    Input           All rotations       Sorted rotations        Output
    easy-peasy$     easy-peasy$         $easy-peasy             yyeep$-aass
                    $easy-peasy         -peasy$easy
                    y$easy-peas         asy$easy-pe
                    sy$easy-pea         asy-peasy$e
                    asy$easy-pe         easy$easy-p
                    easy$easy-p         easy-peasy$
                    peasy$easy-         peasy$easy-
                    -peasy$easy         sy$easy-pea
                    y-peasy$eas         sy-peasy$ea
                    sy-peasy$ea         y$easy-peas
                    asy-peasy$e         y-peasy$eas

    The Burrows-Wheeler algorithm is valuable not only because it allows
    introducing more repetitions in the line (we can achieve even better results
    by simple sorting of all characters), but, with Burrows-Wheeler transform
    you can easily and unambiguously recreate the original text. Your task is
    to print out the original text.

    Input: a string that contains a text transformed using the Burrows-Wheeler
    algorithm. The end of each line is marked with ‘|’ symbol and it should be
    stripped before you start to process the string.

    Output: a string with the original text.

    CONSTRAINTS:
        1. The length of each line is from 5 to 1500 characters.
        2. The sorting order of the characters is defined by their ASCII code,
        that is the character $ (code 36) goes before the letters of the
        alphabet.
'''


def bwt(text, splitter=''):
    text = text.strip()
    bwt = []
    for i in range(len(text)):
        bwt.append(text[-i:] + text[:-i])
    bwt.sort()
    return ''.join(item[-1] for item in bwt) + splitter


def inverse_bwt(code, eof='$', splitter=''):
    code = list(code.strip(splitter + '\n'))
    bwt = code.copy()
    # recreate the list of all rotations
    for i in range(len(code) - 1):
        sorty = sorted(bwt)
        bwt = [''.join(pair) for pair in zip(code, sorty)]
    # find an item with the original text
    for rotation in bwt:
        if rotation.endswith(eof):
            return rotation


if __name__ == '__main__':
    test_cases = [('yyeep$-aass|', 'easy-peasy$'),
                  ('oooooooo$  ffffffff     ffffffffuuuuuuuuaaaaaaaallllllll' \
                   'bbBbbBBb|',
                   'Buffalo buffalo Buffalo buffalo buffalo buffalo Buffalo ' \
                   'buffalo$'),
                  ('edarddddddddddntensr$  ehhhhhhhhhhhJ aeaaaaaaaaaaalhtf th' \
                   'mbfe           tcwohiahoJ eeec t e |',
                   'James while John had had had had had had had had had had ' \
                   'had a better effect on the teacher$'),
                  ('ooooio,io$Nnssshhhjo  ee  o  nnkkkkkkii |', 'Neko no ko ' \
                   'koneko, shishi no ko kojishi$'),
                  ('..fnsyees,,nrff,to,rdsedoseyssnleasdeyr,e,soyotdnheayelgh' \
                   'lektsnynyrofaoueerlrenmtoyfysefnhrmersdtsoosdtn,eeeadt.ys' \
                   'seestostu $     mmmmthhh  mh   tr  lpp  hclp hreerlrnhedw' \
                   'd       iie   iernnenn  n  nebkhhhhslhrhhkhnbwtrerrddrwer' \
                   'r ldhr cggthtpdpmtl hIoooooef  nnnuaea   ectcssst t ttttt' \
                   '  ttttwwwtt tt wtghhthw   a gvttphhhhh  hggwlraallllccsi ' \
                   ' oaiaaao lAloei e do iiiaooaaio aaaaeuiioa eaattgtttsttc ' \
                   '    phrcii l-r mwfn Yyhyvl m oox  oeeeeeuutetiiouggagf of' \
                   'peaoaaaieaiiiisyiucetiussea   ileaar inourararrr saaaai  ' \
                   '       o      iaa       ssharrooo oots baa  o       eltte' \
                   'nanbba  a|',
                   'If a freedman or any other stranger has a property ' \
                   'greater than the census of the third class, at the ' \
                   'expiration of thirty days from the day on which this ' \
                   'comes to pass, he shall take that which is his and go his' \
                   ' way, and in this case he shall not be allowed to remain ' \
                   'any longer by the magistrates. Also the greater part of ' \
                   'politics they imagine to co-operate with nature, but in a' \
                   ' less degree, having more of art, while legislation is ' \
                   'declared by them to be wholly a work of art. You shall ' \
                   'endeavour to impart your thoughts to us, and we will make' \
                   ' an effort to understand you.$'),
                  ('g..fe..ed,yt,tgnudooyd,dyederfoeeorye-edlesodesdee,tdsene' \
                   'ehlfoosedneteselyltfeetetrt,e,,ndfettyfntfdfssmtteetyer.n' \
                   'nstmnd sewes      $ r  g  md   l ec ehehheelhLmm     ia  ' \
                   '  oin esiaocnlleeleenlnne iI     nrhdshhhfbhlbrhhhvnnchbh' \
                   'hbnmhcldlrrddptthrilsTbhhhhmmsmthtpshitdhnolooooooineanna' \
                   'e  twtt ttTtttt t tts tttttwcw  s sssstlchllh  h    akrlm' \
                   ' vstc h  dnngml  llllpsuruuibp efo p aeaaeefees    h rrii' \
                   'i iioiieeiaaaaAiiii iiouu  ieeaeatttntNt d       his twwp' \
                   'nyhhhbll m im   eooepouggdtoeeuiriiwineadiemsaii   s i  a' \
                   'oeeuausnsoauaauixnaancfesa              e cn     acoooopp' \
                   'scjobBaio     aebalanbm |',
                   'The discipline of pleasure is implanted chiefly by the ' \
                   'practice of the song and the dance. But the living - he ' \
                   'should be helped by all his kindred, that while in life ' \
                   'he may be the holiest and justest of men, and after death' \
                   ' may have no great sins to be punished in the world below' \
                   '. No mention occurs in the Laws of the doctrine of Ideas.' \
                   ' And then, again, that the legislator should not permit ' \
                   'them to determine what punishment is to be inflicted in ' \
                   'any of these cases, but should himself decide about all ' \
                   'of them, small or great, is next to impossible. Tell me ' \
                   'whether you assent to my words.$')]

    for i, test in enumerate(test_cases):
        assert inverse_bwt(test[0], splitter='|') == test[1], \
            'failed test No.%d' % i
        assert bwt(test[1], '|') == test[0], 'failed test No.%d' % i
    else:
        print('Test has been passed.')

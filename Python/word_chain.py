'''                                 == EN ==
    In this challenge, we suggest playing "Word chain" - a well-known game in
    which players come up with words that begin with the letter that the
    previous word ended with. Your task is to determine the maximum length of a
    chain that can be created from a list of words.

    Input: a string with a list of words separated by comma.

    Output: a string with the length of the longest chain or "None" if there is
    no chain.

    CONSTRAINTS:
        1. The length of a list of words is in a range from 4 to 35.
        2. A word in a list is represented by a random lowercase ASCII string
            with the length from 3 to 7 letters.
        3. The words in a list do not repeat.
'''


'''                             == Action Plan ==
    1. After some hesitations recursive function was chosen as the most suitable
        solution.
    2. In case we don't know what word is the first in the chain, we'll check
        every word to get the correct result.
'''


def chain(word, words_list, count=1):
    # find next word(s) in the chain
    extension = [w for w in words_list if w[0] == word[-1]]
    if extension:
        cnt = count
        # try every possible variant of continuation
        for w in extension:
            words_list_copy = words_list[:]
            words_list_copy.remove(w)
            count = max(count, chain(w, words_list_copy, cnt + 1))
    return count


def main(words):
    # shorten words to save memory (we need only the first and the last letter)
    words = [word[0] + word[-1] for word in words.strip().split(',')]
    count = 1
    # check every word as the begining of the chain
    for word in words:
        words_copy = words[:]
        words_copy.remove(word)
        count = max(count, chain(word, words_copy))
    return str(count) if count > 1 else 'None'


if __name__ == '__main__':
    test_cases = [('soup,sugar,peas,rice\n', '4'),
                  ('ljhqi,nrtxgiu,jdtphez,wosqm\n', 'None'),
                  ('cjz,tojiv,sgxf,awonm,fcv\n', '2'),
                  ('ehgpw,jwfbz,fqh,epx,dkob,skbud,jmeidb,qrly,rduzt,yearwdt,' \
                   'lxpqmr,oaucjbl,adk,heidog', '3'),
                  ('jop,sqydzpx,awxjgp,fhrvaoe,wpn,mdbinvu,ufipbt,pvlqiej,' \
                   'mfwe,ukezh,lgu', '3'),
                  ('wyrvjxdd,weoscmird,wydrd,wtxeusjd,wvwlbtd,wnwspxd,' \
                   'wkhalfsvd,wljacbd,wmwkad,wnkud,wzohjiked,wifnaltd', 'None'),
                  ('apz,yglokh,ayhs,sfydw,kzdbjvi,prt,lraivtw,boitz,szu,vrio,' \
                   'sweh,gvybp,jgd,tufh,svyj,gxtmey,ponhi,ldixm,rno,qwi,' \
                   'dlvchxw,zjurqw,qlnck,tyhoul,fpaon,fyrup,itoe,ejtg,gtucp,' \
                   'adyegs,eriao,epvy,ctj', '8')]

    for test in test_cases:
        assert main(test[0]) == test[1], 'failed %s' % test[0]
    else:
        print('Test has been passed.')

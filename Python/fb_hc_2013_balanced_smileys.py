'''                                 == EN ==
    Credits: This problem appeared in the Facebook Hacker Cup 2013 Hackathon.

    Your friend John uses a lot of emoticons when you talk to him on Messenger.
    In addition to being a person who likes to express himself through
    emoticons, he hates unbalanced parenthesis so much that it makes him go :(.

    Sometimes he puts emoticons within parentheses, and you find it hard to tell
    if a parenthesis really is a parenthesis or part of an emoticon. A message
    has balanced parentheses if it consists of one of the following:

        - An empty string ""
        - One or more of the following characters: 'a' to 'z', ' ' (a space) or
            ':' (a colon)
        - An open parenthesis '(', followed by a message with balanced
            parentheses, followed by a close parenthesis ')'.
        - A message with balanced parentheses followed by another message with
            balanced parentheses.
        - A smiley face ":)" or a frowny face ":("

    Write a program that determines if there is a way to interpret his message
    while leaving the parentheses balanced.

    Input: a string with a message that you got from John.

    Output: the string "YES"/"NO" (all quotes for clarity only) stating whether
    or not it is possible that the message had balanced parentheses.
'''


# stack-based version
def smiley(string):
    # to avoid check for last index in string in every single iteration
    if not string.endswith('\n'):
        string += '\n'
    stack = []
    i = 0
    while i < len(string.rstrip()):
        char = string[i]
        if char == '(':
            # what to look for ([kind_of_parenthesis, flag])
            #   flags: 0 - unmatched yet, 1 - possible match)
            stack.append([')', 0])
        elif char == ')':
            if stack and stack[-1][0] == char:
                # strict match: delete from stack
                for j in range(1, len(stack) + 1):
                    if stack[-j][1] == 0:
                        stack.pop(-j)
                        break
                else:
                    # if there are only possible matches in stack
                    stack.pop(-1)
            else:
                break
        elif char == ':':
            next_char = string[i + 1]
            if next_char in '()':
                if next_char == ')':
                    if stack and stack[-1][0] == next_char:
                        # change the flag to 'possible match'
                        stack[-1][1] = 1
                else:
                    # got possible open parenthesis
                    stack.append([')', 1])
                i += 2
                continue
        i += 1
    else:
        return 'YES' if not stack or all(i[1] == 1 for i in stack) else 'NO'
    return 'NO'


# optimized version
def smiley2(string):
    min_to_close = max_to_close = 0
    for i, char in enumerate(string):
        if char == '(':
            max_to_close += 1
            if i == 0 or string[i - 1] != ':':
                min_to_close += 1
        elif char == ')':
            min_to_close = max(0, min_to_close - 1)
            if i == 0 or string[i - 1] != ':':
                max_to_close -= 1
                if max_to_close < 0:
                    break
    return 'YES' if max_to_close >= 0 and not min_to_close else 'NO'


if __name__ == '__main__':
    test_cases = [
        ('a(ba::b()b()a(c((():b:acc(ab: :) aa()aa  c)a cb:(cc((abbc:a))ab)( (' \
         ' :cc::bb(:a:))b)aab:(: (', 'NO'),
        ('(c(baac)bcc(()bb a) cacbacccc::c)a( (:bac()::ac(:(():(bba:c(cccbbba' \
         'cab)b)c ))b::cb(acb):)ab:c', 'YES'),
        ('(aca(baccb()()):c( (:a(aab)cac:b:bccbb(a (())c()a:ab:)c)a)ca)a:acb ' \
         ':::(b:)cc(b:b:b)):cb)', 'YES'),
        ('(:a))', 'NO'),
        ('b)::):b:bc)bbaa):aacca):c:a )))(:b()ab(acac b acca(b::ba  c)bab(bc)' \
         ':c::a(()a:b:b)a()cc)(( babcc', 'NO'),
        ('b:(b::ba((c:a:acbcc)b:)(()acc:)a:))b((b( (:)c)ba):cc()::(ca)ccb: :(' \
         ':((:b)()acca ):b)a:', 'YES'),
        (':(bb)(b(a::)c:)aab (:b  bccc(accacacbcb((c)a):))cb:(abbb:baa:)ccbbc' \
         ')ca)cab:b(c(:( :)aca):ba:b::c)a:a', 'YES'),
        ('(:((c((ca):(b(a((acbb)b(a))c))b )ca:b::a )a:c)bca:(b b:a b:)): :)b(' \
         '(a)()c:)a:(ab(:)cb:c)   ):::a', 'YES'),
        ('cb())(cca(b()::c)aab:ab)()b(:a(bc(ac)cca)b :::cc((bb:()bbb ))()cb):' \
         'c)b(()b:(bcb):cbbc)c a', 'NO'),
        ('baac:()a(a): (a ccb:(:c)ac)b:a(a (a:( bb:)c(a):ca)c:bba)abb::cca cc' \
         '():)b )b(:::)', 'YES'),
        ('a(:((ca)ccbcb()ca:b)(b:a:):b:bcc:a : ba( aa(:aa)()( ccacb()abb() )b' \
         '))bbaa cb(ab(::aa:cab:bcb))cc:b', 'YES'),
        ('b )aac(b(acb )bb:(a b:)  b ):b)))ab((:b(cc:a )a:a):ac:()b)((b())a(b' \
         ')c:)(aba:::aa:)):::cbac)::aaab', 'NO'),
        ('c(:)ba(( c(:cca):bab(:c((acc :()abb(bb)a)ba)))(a) a::aa(:)()(( abbc' \
         ':)))cc::b):))) cbac', 'YES'),
        (':abba( )caa:bcabcbb:caa)a:))a(ac(bcab()c:)abb):a:ccca ca:b((c)))aa)' \
         'c:c:b):aa))bb)cbba bc ca(c ab:', 'NO'),
        ('bc)(aa:(a (c(:()a()((a a:ac)c))ba(a)a::) ::)b:b)b)ba(:():))c:abb:)a' \
         'a:bac())cba( b(  )(((c:c:b)', 'NO'),
        ('bbcbcb(c:b :)(bc::ba) )()aa:bbbb :a:acacb( bc(c)((:a:ac(::)a)a:()c:' \
         'c()a(a))::a)cb:b:bba(a)b', 'YES'),
        ('(bc)(::c bbaccc(::ca:(:(:cc)cbaaaccca(:(ac): c:bbbb :(caababb(()a((' \
         'accba(:bca)cabb)', 'NO')]

    for i, test in enumerate(test_cases):
        assert smiley(test[0]) == test[1], 'failed test no.%d' % i
        assert smiley2(test[0]) == test[1], 'failed test no.%d' % i

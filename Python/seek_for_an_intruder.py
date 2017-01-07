'''                                 == EN ==
    A company's server has been down for a couple of hours due to an
    unauthorized intrusion. After bringing it back live, a security department
    started to investigate the log files in order to find any trails of a
    hacker. Luck was on their side: they found a broken network log file
    containing pieces of useful data that could possibly help them identify an
    intruder. Among the garbage of ASCII uppercase and lowercase letters,
    punctuation marks, and digits, they found IP addresses in various formats.

    For example:
        Dotted decimal	192.0.2.235 with no leading zero.
        Dotted hexadecimal 0xc0.0x0.0x02.0xeb Each octet is individually
            converted to hexadecimal form.
        Dotted octal 0300.0000.0002.0353 Each octet is individually converted
            into octal.
        Dotted binary 11000000.00000000.00000010.11101011 Each octet is
            individually converted into binary.
        Binary 11000000000000000000001011101011
        Octal 030000001353
        Hexadecimal	0xC00002EB	Concatenation of the octets from the dotted
            hexadecimal.
        Decimal	3221226219	The 32-bit number expressed in decimal.

    To help them finish their investigation and find the hacker, you need to
    find the most frequently occurring IP address in that file. You must search
    only for a valid IPv4 address in a range from 1.0.0.0 to 255.255.255.254.

    Your program should accept as its first argument a path to a filename. The
    file contains the N number of lines with the length of M symbols.

    Print out the most frequently occurring IP address in a dotted decimal
    representation without leading zeros. In case there is more than one most
    frequently occuring IP address, then print them both out in ascending order
    separated by a white space.

    Constraints:
        M is in range [100, 300]
        N is in range [800, 1200]
'''


from re import IGNORECASE, findall


def int2ip(ipint):
    return '.'.join([str(ipint >> (i << 3) & 0xFF) for i in range(4)[::-1]])


def ip2int(ipstr):
    return sum(int(octet) << r for octet, r in
               zip(ipstr.split('.'), range(24, -1, -8)))


def make_ip(ip, base):
    return '.'.join(str(int(octet, base)) for octet in ip.split('.'))


IP_RANGE = range(ip2int('1.0.0.0'), ip2int('255.255.255.255'))
BASE = (10, 16, 8, 2, 10, 16, 8, 2)


def ip_validator(ip_list):
    valid_ip = {}
    for group in ip_list:
        for tip, ip in enumerate(group):
            if not ip:
                continue

            if tip < 4:
                if all(int(octet, BASE[tip]) in range(255 if i < 3 else 254)
                       for i, octet in enumerate(ip.split('.'))):
                    ip = ip2int(make_ip(ip, BASE[tip]))
                else:
                    continue
            else:
                ip = int(ip, BASE[tip])
                if ip not in IP_RANGE:
                    continue

            if ip in valid_ip:
                valid_ip[ip] += 1
            else:
                valid_ip[ip] = 1

    most_frequent = max(count for ip, count in valid_ip.items())
    return sorted(ip for ip, count in valid_ip.items()
                  if count == most_frequent)


def main(log):
    ip_list = []
    for line in log.split('\n'):
        ip_list += findall(
            '(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})|' \
            '(0x[a-f\d]{1,2}\.0x[a-f\d]{1,2}\.0x[a-f\d]{1,2}\.0x[a-f\d]{1,2})|'\
            '(0\d{3}\.0\d{3}\.0\d{3}\.0\d{3})|' \
            '([01]{8}\.[01]{8}\.[01]{8}\.[01]{8})|' \
            '(\d{8,10})|' \
            '(0x[a-f\d]{7,8})|' \
            '(0\d{9,11})|' \
            '([01]{25,32})',
            line, IGNORECASE
        )
    return ' '.join(int2ip(ip) for ip in ip_validator(ip_list))


if __name__ == '__main__':
    test_case = "m*M}Qz`\fz/We}e[`md;Puuat-;UP|Yi64iXh%{Hnul8&onq0p*mY+4x\/{ZTw[gXeJV2&.P*Ywe\n" \
                "VA,8Z%z-AYzp6o{qeX3Q|\`Zw7{78:Y80qP-,b0BDVvZh60x59.0xe5.0x82.0xe1uptW8eF8C]nKJ9c(AtXa9>Dy}nF'Jr\n" \
                "Cq2ox2Mmr7PuaPO023244514100.@({-mER/yhWg)wsf\"`Fu_tp.C]6$!?(^+wzLBxi,PJ41Hdu`m>Bz=v*^~N|h\n" \
                "jfZ&y9w'XkrrO6JDoZOyZ864.599.341.917JBJ5u(^i%BjecAd\"$4UKtPnbtvx^01540.01127.0525.01625tU$HY/,Uw(/CJP]L+/XohV2hD&]\n" \
                "9Pl.1011001111001011000001011100001,Y,HNAiSzL;?BU_UQlCvyzRU^\"R]{kVJ\"[+3%PK`]\"V?;Y'8CjJ<&QGmESP6W7&P,@$tFtL\n" \
                "`z6DR}/>gLfLX[1&]Vr8\"EG-_+wy?sw4beHIp^oTtZzvWBwY{[89.229.130.225R,?B;\"?[ix4^9D$fVaJ_V\)N`B\n" \
                "=ddalCNOM)FnA=/r,?}#idpo1E#eeMq.wyfu/2viz;c_[kHppMh,K|\`Q1_R(`jRNvCZW2Niz7Q#\n" \
                "w:b21f[rsnj^Rgg[t!(<5v`Iup^&]o@489.229.130.225gw4\SwBEbN222.137.104.206[Jo<)lj36bB.034062405073xx37d;~wKi/D\"I'AeVfeBO\n" \
                "|7$mi3k]f}9N*Vjq5aMy[Xd+3a$n$paB?5p9^01000000.11101110.00100000.01100101u@0:7&J;8FDZ<LuN-ecftQ%XU2urHk=N\"y}1Zt+\n" \
                "|lLN|l8ZlMi()kN29/B!uj~l8#1o?Kcp/1{FfL]1/NsK$<@`)0P+LVgv4ziP>t840131.0345.0202.0341`}Z*Xz[8IH?'\n" \
                "^~H5]JqL#?>d8V5JPP1101100000.1001010111.101010101.11100101011Funfr=3*E\pEa\"3YV^?J+;dLA#t)$3Lvi5J<MSF]LB&yOXgO't/E864.599.341.917Ze033642264316z~7\n" \
                "W7+1&dt2#Ek&<am6G|!!18P>?|?qQyV(0k?>KPB:t{IRUm>cuN0^[YSOsixxF\"zzl5LALPIaXFM.\n" \
                "jMfgpfH+w>M8\`r{;`XdEYm0Rc7o>Aqq4k?gP>,O^2I^]OF#zN\cLSUQ(x!(oxA0l<xjM=-qcIXE\n" \
                "_L)a,<}f4u9dc]'440h0y7Yu=&NOfz-k%hk/FLpVZBsX|+P5YjaNBH]TCG~{,k]Dc\7p$)s&4D+Y\n" \
                "xI~0JkBd]}c#]!4eGec7oz>d:yYl*K_AK^Hd_<c+hjD4w:-[90?}lBZ]^@iT2A&i9=9tsjg3muNC\n" \
                ",6ze^#eqtjrd`P&?WY,J-]L)_gVR*NJ~]Q(#l\"Yu~Jpl*ui\"9JtZ=&2B{!6\"iP@Y@3I%Zft>cpd`\n" \
                "OwEK!d?y\M(_L~|=lm1++BLA<&PnOnBAfga>t},x{T$*&/}+wX{j/pm'|N~Cq1000000111011100010000001100101x~[*Scc=lb82`K~\n" \
                "HydTS#@@864.599.341.917Q&.DVb\ails}C101100100110010011011000101110100&@KyFK\"7}u3\63?u][~zz>-r$_OqUbE*uv,\ccCnUmP\<p,o4E6[7c]\n" \
                "v<md%aG2z8n'}\"9}qwZYnHdo>`4/Ht!3puL.A\'].BA>reos{U0x360.0x257.0x155.0x395y^UGXh^'`|I.CV}R>a}RAhO%Vw\n" \
                "uQ#27/z^B8q:x(I|$k9dmF{\<ofV5sg[F>P(t!ui5[<mpXTzO%0wF|E2Sh6bl5[YZ:Tm%JsE*5pUO\n"

    answer = '89.229.130.225'

    assert main(test_case) == answer, 'test failed'
    print('Test has been passed.')

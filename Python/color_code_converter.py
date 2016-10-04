'''                                 == EN ==
    Your task is to write a program which converts different types of color
    codes, such as CMYK, Hex, HSL, HSV, and RGB. The converter should accept
    codes formatted as follows:

        HSL: "HSL(D,P,P)"
        HSV: "HSV(D,P,P)"
        CMYK: "(F,F,F,F)"
        Hex: "#000000"

    Where:
        'D' is in range [0, 359] degrees,
        'P' is in range [0, 100] percent,
        'F' is a float, rounded to a second digit after dot in range
            [0.00, 1.00],
        Hex is in range [#000000, #ffffff]

    Input: a string with color code.

    Output: determine the color code, convert it to RGB, and return a string
    with RGB code formatted as follows "RGB(255,255,255)". You must round all
    floating-point numbers, if any, to integers.

    CONSTRAINTS:
        1. Assume all input has the correct form.
'''


from colorsys import hls_to_rgb, hsv_to_rgb


def rgb_format(r, g, b):
    return 'RGB(%d,%d,%d)' % (r, g, b)


def hs_to_rgb(hs_string, key):
    '''
    Convert HSL or HSV to RGB.

    Keys: l - for HSL, v - for HSV
    '''
    key = key.lower()
    if key not in ('l', 'v'):
        return ''
    pattern = 'hs{}()'.format(key)
    converter = hls_to_rgb if key == 'l' else hsv_to_rgb
    code = [int(c) / 100 if i > 0 else int(c) / 360
            for i, c in enumerate(hs_string.strip(pattern).split(','))]
    if key == 'l':
        code.insert(1, code.pop(-1))
    rgb = converter(*code)
    r, g, b = (round(c * 255) for c in rgb)
    return rgb_format(r, g, b)


def cmyk_to_rgb(cmyk_string):
    c, m, y, k = [float(c) for c in cmyk_string.strip('()').split(',')]
    r, g, b = [round(255 * (1 - i) * (1 - k)) for i in (c, m, y)]
    return rgb_format(r, g, b)


def hex_to_rgb(hex_string):
    r, g, b = [int(hex_string[i:i + 2], 16)
               for i in range(1, len(hex_string), 2)]
    return rgb_format(r, g, b)


def color_converter(string):
    string = string.strip().lower()
    if string.startswith('hsl('):
        rgb = hs_to_rgb(string, 'l')
    elif string.startswith('hsv('):
        rgb = hs_to_rgb(string, 'v')
    elif string.startswith('('):
        rgb = cmyk_to_rgb(string)
    elif string.startswith('#'):
        rgb = hex_to_rgb(string)
    else:
        return 'Not supported color format'
    return rgb


if __name__ == '__main__':
    test_cases = [('(0.56,0.94,0.21,0.02)\n', 'RGB(110,15,197)'),
                  ('HSL(359,0,0)\n', 'RGB(0,0,0)'),
                  ('HSV(276,33,7)\n', 'RGB(15,12,18)'),
                  ('#cfa9c4\n', 'RGB(207,169,196)'),
                  ('HSL(291,66,74)', 'RGB(219,145,232)'),
                  ('HSV(65,72,73)', 'RGB(175,186,52)'),
                  ('(0.97,0.35,0.55,0.77)', 'RGB(2,38,26)'),
                  ('#f04188', 'RGB(240,65,136)'),
                  ('(1.00,1.00,0.90,0.20)', 'RGB(0,0,20)'),
                  ('HSL(218,9,67)', 'RGB(163,169,178)'),
                  ('red', 'Not supported color format')]

    for i, test in enumerate(test_cases):
        assert color_converter(test[0]) == test[1], 'failed test No. %d' % i
    else:
        print('Test has been passed.')

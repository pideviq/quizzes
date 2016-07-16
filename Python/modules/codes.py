################################################################################
############                         Codes                          ############
#######                  different code alphabets module                 #######
################################################################################

#------------------------------------------------------------------------------#
#                                    MORSE                                     #
#------------------------------------------------------------------------------#
morseRU = {'А': '.-',               'К': '-.-',             'Х': '....',
           'Б': '-...',             'Л': '.-..',            'Ц': '-.-.',
           'В': '.--',              'М': '--',              'Ч': '---.',
           'Г': '--.',              'Н': '-.',              'Ш': '----',
           'Д': '-..',              'О': '---',             'Щ': '--.-',
           'Е': '.',                'П': '.--.',            'Ъ': '-..-',
           'Ё': '.',                'Р': '.-.',             'Ы': '-.--',
           'Ж': '...-',             'С': '...',             'Ь': '-..-',
           'З': '--..',             'Т': '-',               'Э': '..-..',
           'И': '..',               'У': '..-',             'Ю': '..--',
           'Й': '.---',             'Ф': '..-.',            'Я': '.-.-'}

ruMORSE = {                               '.': 'Е',
                      '..': 'И',                            '.-': 'А',
           '...': 'С',         '..-': 'У',        '.-.': 'Р',        '.--': 'В',
           '....': 'Х',       '...-': 'Ж',        '..-.': 'Ф',      '..--': 'Ю',
           '.-..': 'Л',       '.-.-': 'Я',        '.--.': 'П',      '.---': 'Й',
           '..-..': 'Э',
                                          '-': 'Т',
                      '-.': 'Н',                            '--': 'М',
           '-..': 'Д',         '-.-': 'К',        '--.': 'Г',        '---': 'О',
           '-...': 'Б',       '-..-': 'Ь',        '-.-.': 'Ц',      '-.--': 'Ы',
           '--..': 'З',       '--.-': 'Щ',        '---.': 'Ч',      '----': 'Ш'}

morseEN = {'A': '.-',               'J': '.---',            'S': '...',
           'B': '-...',             'K': '-.-',             'T': '-',
           'C': '-.-.',             'L': '.-..',            'U': '..-',
           'D': '-..',              'M': '--',              'V': '...-',
           'E': '.',                'N': '-.',              'W': '.--',
           'F': '..-.',             'O': '---',             'X': '-..-',
           'G': '--.',              'P': '.--.',            'Y': '-.--',
           'H': '....',             'Q': '--.-',            'Z': '--..',
           'I': '..',               'R': '.-.'}

enMORSE= {                               '.': 'E',
                          '..': 'I',                            '.-': 'A',
               '...': 'S',         '..-': 'U',        '.-.': 'R',        '.--': 'W',
           '....': 'H', '...-': 'V', '..-.': 'F', '.-..': 'L', '.--.': 'P', '.---': 'J',

                                          '-': 'T',
                          '-.': 'N',                            '--': 'M',
               '-..': 'D',         '-.-': 'K',        '--.': 'G',        '---': 'O',
           '-...': 'B', '-..-': 'X', '-.-.': 'C', '-.--': 'Y', '--..': 'Z', '--.-': 'Q'}

morseNUM = {'1': '.----',           '6': '-....',
            '2': '..---',           '7': '--...',
            '3': '...--',           '8': '---..',
            '4': '....-',           '9': '----.',
            '5': '.....',           '0': '-----'}

numMORSE = {'.----': '1',           '-....': '6',
            '..---': '2',           '--...': '7',
            '...--': '3',           '---..': '8',
            '....-': '4',           '----.': '9',
            '.....': '5',           '-----': '0'}

morseSGN = {'.': '.-.-.-',          "'": '.----.',
            ',': '--..--',          '(': '-.--.',
            '?': '..--..',          ')': '-.--.-',
            ':': '---...',          '=': '-...-',
            ';': '-.-.-.',          '+': '.-.-.',
            '-': '-....-',          '$': '...-..-',
            '/': '-..-.',           '!': '--..--',
            '"': '.-..-.',          '_': '..--.-'}

sgnMORSE = {'.-.-.-': '.',          '.----.': "'",
            '--..--': ',',          '-.--.':  '(',
            '..--..': '?',          '-.--.-': ')',
            '---...': ':',          '-...-':  '=',
            '-.-.-.': ';',          '.-.-.':  '+',
            '-....-': '-',          '...-..-': '$',
            '-..-.':  '/',          '--..--': '!',
            '.-..-.': '"',          '..--.-': '_'}

morseENCODE = {}
morseENCODE.update(morseRU)
morseENCODE.update(morseEN)
morseENCODE.update(morseNUM)
morseENCODE.update(morseSGN)

morseDECODE_RU = {}
morseDECODE_RU.update(numMORSE)
morseDECODE_RU.update(sgnMORSE)
morseDECODE_RU.update(ruMORSE)

morseDECODE_EN = {}
morseDECODE_EN.update(numMORSE)
morseDECODE_EN.update(sgnMORSE)
morseDECODE_EN.update(enMORSE)


#------------------------------------------------------------------------------#
#                                  ROMAN NUMS                                  #
#------------------------------------------------------------------------------#
roman = {'I': 1,            1: 'I',
         'V': 5,            5: 'V',
         'X': 10,          10: 'X',
         'L': 50,          50: 'L',
         'C': 100,        100: 'C',
         'D': 500,        500: 'D',
         'M': 1000,      1000: 'M'}

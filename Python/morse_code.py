import modules.codes as codes


class Morse:
    '''
    Morse alphabet encoding/decoding functions
    '''
    def decode(self, code, lang='EN'):
        '''
        Decode dot-and-dash sequense
        '''
        if len(code) < 1: return ''
        lang = lang.lower()
        if lang == 'en':
            morseDECODE = codes.morseDECODE_EN
        elif lang == 'ru':
            morseDECODE = codes.morseDECODE_RU
        else:
            return ''

        phrase = []
        words  = code.split('  ')
        for word in words:
            if not word: continue
            letters = word.strip().split(' ')
            wrd = ''
            for letter in letters:
                if letter in morseDECODE:
                    wrd += morseDECODE[letter]
                else:
                    print('\nSorry, can\'t decode this code.')
                    return ''
            phrase.append(wrd)
        return ' '.join(phrase)


    def encode(self, text):
        '''
        Encode text into dot-and-dash sequense
        '''
        if len(text) < 1: return ''
        text = text.upper()
        morseENCODE = codes.morseENCODE

        code  = []
        words = text.split(' ')
        for word in words:
            if not word: continue
            wrd = []
            for letter in word:
                if letter in morseENCODE:
                    wrd.append(morseENCODE[letter])
                else:
                    print('\nSorry, can\'t encode this code.')
                    return ''
            code.append(' '.join(wrd))
        return '    '.join(code)


if __name__ == '__main__':
    import modules.cmd_ui as ui

    menu  = ['encode to Morse', 'decode Morse']
    morse = Morse()

    def game():
        '''
        Game cicle function
        '''
        choice = ui.cmdMenu('Morse Coding', menu)

        if choice == 1:
            text = ui.getInput('\nType text for encoding:\n')
            print('\n', morse.encode(text))

        elif choice == 2:
            code = ui.getInput('\nType morse code for decoding:\n', '.-')
            lang = ui.getInput('\nChoose language for decoding (en/ru): ', ('en', 'ru'))
            print('\n', morse.decode(code, lang))

        if ui.onceMore(): game()


    game()

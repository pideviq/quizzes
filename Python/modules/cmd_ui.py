from sys import exit
from re  import match


def cmdMenu(name, menuList):
    '''
    Launch simple command line user interface
    '''
    print('\nWelcome to %s!' % name)
    for n, item in enumerate(menuList, 1): print('%d - %s' % (n, item))

    while True:
        print('\n' + '#' * 40)
        choice = input('\nChoose the mode: ')
        if not choice: break
        elif not choice.isdigit():
            print('\nMode should be a digit.')
            continue
        elif int(choice) not in range(1, len(menuList) + 1):
            print('\nMode number is out of range.')
            continue
        return int(choice)

    input('Press Enter to exit.')
    exit()


def getInput(query, legal='', case=False):
    '''
    Get and check user input
    '''
    answer = input(query)
    return checkInput(answer, query, legal, case)


def _checkInput(answer, query, legal='', case=False):
    '''
    Check the correctness of input
    (based on regular expressions method)
    '''
    if not case: answer = answer.lower()

    if legal:
        if type(legal) == str:
            strict  = match('([\w\s]*)(\W*)', legal)
            spec    = strict.group(1) + ''.join(('\\' + s for s in strict.group(2)))
            pat     = '^[%s ]*$' % spec
        elif type(legal) in (int, float):
            pat     = '^[%r ]*$' % legal
        else:
            pat     = '^[%s ]*$' % '|'.join(legal)

        if not match(pat, answer):
            print('\nIncorrect input. Try once more.\n')
            answer = getInput(query, legal)

    return answer


def checkInput(answer, query, legal='', case=False):
    '''
    Check the correctness of input
    '''
    if not case: answer = answer.lower()

    if legal:
        if type(legal) == str:
            for symb in answer:
                if symb not in legal:
                    print('\nIncorrect input. Try once more.\n')
                    answer = getInput(query, legal)
                    break
        elif type(legal) in (tuple, list):
            if answer not in legal:
                print('\nIncorrect input. Try once more.\n')
                answer = getInput(query, legal)
        else:
            print('\nIncorrect type of legal. Can\'t check the answer.\n')
            return ''

    return answer


def onceMore(query=''):
    '''
    Ask user if he wants to play one more time
    '''
    if not query: query = 'Do you want to play one more time (y/n)?  '
    return True if getInput(query, ('y', 'n')) == 'y' else False


if __name__ == '__main__':
    print('You picked', cmdMenu('Test', ['first', 'second', 'third']))

'''
    В системе авторизации есть ограничение: логин должен начинаться с латинской
    буквы, состоять из латинских букв, цифр, точки и минуса, но заканчиваться
    только латинской буквой или цифрой; минимальная длина логина — один символ,
    максимальная — 20. Напишите код, проверяющий соответствие входной строки
    этому правилу. Придумайте несколько способов решения задачи и сравните их.
'''

#============================   First variant   ===============================#
import re

def checkLogin(login):
    '''
    Login validation function
    '''
    if len(login) not in range(1, 21): return False
    if re.match(r'(^[A-Za-z]+[A-Za-z\d.-]*[A-Za-z\d]{1}$)', login):
        return True
    else:
        return False


#===========================   Second variant   ===============================#
from string import ascii_letters, digits

signs   = '.-'
allowed = ascii_letters + digits + signs

def checkLogin2(login):
    '''
    Login validation function
    '''
    if len(login) not in range(1, 21): return False
    if login[0] not in ascii_letters or login[-1] not in (ascii_letters + digits):
        return False

    for symbol in login[1:-1]:
        if symbol not in allowed: return False

    return True


if __name__ == '__main__':
    assert checkLogin('app1e') == True, 'checkLogin'
    assert checkLogin('0e.g-g') == False, 'must start with latin letter'
    assert checkLogin('Apple-') == False, 'must end with latin letter or number'
    assert checkLogin('App$e') == False, 'should contain only latin letters, numbers, "." or "-"'
    assert checkLogin('') == False, 'login length must be at least 1 charackter'
    assert checkLogin('abcdefghklmnopqrstuvwxyz') == False, 'login length should be less than 20 charackters'

    assert checkLogin2('app1e') == True, 'checkLogin'
    assert checkLogin2('0e.g-g') == False, 'must start with latin letter'
    assert checkLogin2('Apple-') == False, 'must end with latin letter or number'
    assert checkLogin2('App$e') == False, 'should contain only latin letters, numbers, "." or "-"'
    assert checkLogin2('') == False, 'login length must be at least 1 charackter'
    assert checkLogin2('abcdefghklmnopqrstuvwxyz') == False, 'login length should be less than 20 charackters'

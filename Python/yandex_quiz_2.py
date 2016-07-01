'''
    В системе авторизации есть ограничение: логин должен начинаться с латинской
    буквы, состоять из латинских букв, цифр, точки и минуса, но заканчиваться
    только латинской буквой или цифрой; минимальная длина логина — один символ,
    максимальная — 20. Напишите код, проверяющий соответствие входной строки
    этому правилу. Придумайте несколько способов решения задачи и сравните их.
'''

import re

def checkLogin(login):
    if len(login) < 1 or len(login) > 20: return False
    if re.match(r'(^[A-Za-z]+[A-Za-z\d.-]*[A-Za-z\d]{1}$)', login):
        return True
    else:
        return False


if __name__ == '__main__':
    assert checkLogin('app1e') == True, 'checkLogin'
    assert checkLogin('0e.g-g') == False, 'must start with latin letter'
    assert checkLogin('Apple-') == False, 'must end with latin letter or number'
    assert checkLogin('App$e') == False, 'should contain only latin letters, numbers, "." or "-"'
    assert checkLogin('') == False, 'login length must be at least 1 charackter'
    assert checkLogin('abcdefghklmnopqrstuvwxyz') == False, 'login length mustn\'t be more than 20 charackters'

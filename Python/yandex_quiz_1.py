'''
    Есть два списка разной длины. В первом содержатся ключи, а во втором
    значения. Напишите функцию, которая создаёт из этих ключей и значений
    словарь. Если ключу не хватило значения, в словаре должно быть значение
    None. Значения, которым не хватило ключей, нужно игнорировать.
'''

def zipper(a, b):
    '''
        Unite keys list with values list.
        a - list with keys
        b - list with values
    '''
    if len(b) < len(a):
        for i in range(len(a) - len(b)):
            b.append(None)

    return dict(zip(a, b))


if __name__ == '__main__':
    assert zipper(['a', 'b', 'c'], [1, 2, 3, 4]) == {'a': 1, 'b': 2, 'c': 3}, 'zipper'
    assert zipper(['a', 'b', 'c'], [1, 2]) == {'a': 1, 'b': 2, 'c': None}, 'zipper'

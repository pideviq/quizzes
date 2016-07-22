'''                                 == EN ==
    Our Robo-Trio need to train for future journeys and treasure hunts. Stephan
    has built a special flat model of a pyramid. Now the robots can train for
    speed gold running. They start at the top of the pyramid and must collect
    gold in each room, choose to take the left or right path and continue down
    to the next level. To optimise their gold runs, Stephan need to know the
    maximum amount of gold that can be collected in one run.

    Consider a tuple of tuples in which the first tuple has one integer and each
    consecutive tuple has one more integer then the last. Such a tuple of tuples
    would look like a triangle. You should write a program that will help
    Stephan find the highest possible sum on the most profitable route down the
    pyramid. All routes down the pyramid involve stepping down and to the left
    or down and to the right.

    Tips: Think of each step down to the left as moving to the same index
    location or to the right as one index location higher. Be very careful if
    you plan to use recursion here.

    Input: A pyramid as a tuple of tuples. Each tuple contains integers.

    Output: The maximum possible sum as an integer.
'''

'''                                 == RU ==
    Нашему Робо-Трио необходимо тренироваться для будущих приключений и охоты за
    сокровищами (золотые контакты нужны всем). Стефан построил специальную
    упрощенную модель пирамиды. И теперь наши роботы будут тренироваться в
    забегах за золотом на скорость. Они начинают с вершины пирамиды и собирают
    золото в каждой комнате, через которую проходят. В каждой комнате они
    выбирают влево или вправо и спускаются на следующий уровень. Чтобы оценивать
    результаты, Стефану нужно знать, а сколько максимум можно собрать за один
    забег.

    Представьте кортеж (tuple) кортежей в котором первый массив имеет одно число
    и следующие на одно число больше чем предыдущий. Такой кортеж кортежей будет
    выглядеть как треугольник. Вам нужно написать функцию, которая поможет
    Стефану найти максимальную сумму золота на самом выгодном маршруте с вершины
    пирамиды до ее основания. Все маршруты прохода по пирамиде из шагов вниз и
    влево/вправо.

    Примечания: Попробуйте думать о шаге вниз-влево, как о движении в следующий
    ряд не изменяя индекс в ряду и о шаге вниз/вправо - с увеличением индекса в
    ряду на единицу. Будьте осторожны если вы хотите решать задачу рекурсией,
    получится медленное решение.

    Ввод: Пирамида, как кортеж (tuple) кортежей. Каждый кортеж содержит
    целочисленное (int).

    Вывод: Максимально количество золота за один забег, как целочисленное (int).
'''

'''                             == Action Plan ==
    1. Find all possible paths from top to bottom
    2. Count an amount of gold on each path
    3. Find maximum
'''

def count_gold(pyramid):
    """
    Return max possible sum in a path from top to bottom
    """
    from itertools import product

    combos = [(0,) + path for path in product((0, 1), repeat=len(pyramid)-1)]
    results = []

    for combo in combos:
        results.append(sum(pyramid[row][sum(combo[:row+1])] for row in range(len(combo))))

    return max(results)


def count_gold_shorthand(pyramid):
    """
    Return max possible sum in a path from top to bottom
    """
    from itertools import product

    return max(sum(pyramid[row][sum(combo[:row+1])] for row in range(len(combo)))
               for combo in [(0,) + path for path in product((0, 1), repeat=len(pyramid)-1)])


if __name__ == '__main__':
    # These "asserts" using for auto-testing
    test1 = (
        (1,),
        (2, 3),
        (3, 3, 1),
        (3, 1, 5, 4),
        (3, 1, 3, 1, 3),
        (2, 2, 2, 2, 2, 2),
        (5, 6, 4, 5, 6, 4, 3)
    )
    test2 = (
        (1,),
        (2, 1),
        (1, 2, 1),
        (1, 2, 1, 1),
        (1, 2, 1, 1, 1),
        (1, 2, 1, 1, 1, 1),
        (1, 2, 1, 1, 1, 1, 9)
    )
    test3 = (
        (9,),
        (2, 2),
        (3, 3, 3),
        (4, 4, 4, 4)
    )

    assert count_gold(test1) == 23, "First example"
    assert count_gold(test2) == 15, "Second example"
    assert count_gold(test3) == 18, "Third example"

    assert count_gold_shorthand(test1) == 23, "First example (short)"
    assert count_gold_shorthand(test2) == 15, "Second example (short)"
    assert count_gold_shorthand(test3) == 18, "Third example (short)"

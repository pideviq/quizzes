'''                                 == EN ==
    A blacksmith gave his apprentice a task, ordering them to make a selection
    of rings. The apprentice is not yet skilled in the craft and as a result of
    this, some (to be honest, most) of rings came out connected together. Now
    he’s asking for your help separating the rings and deciding how to break
    enough rings to free so as to get the maximum number of rings possible.

    All of the rings are numbered and you are told which of the rings are
    connected. This information is given as a sequence of sets. Each set
    describes the connected rings. For example: {1, 2} means that the 1st and
    2nd rings are connected. You should count how many rings we need to break to
    get the maximum of separate rings. Each of the rings are numbered in a range
    from 1 to N, where N is total quantity of rings.

    For example, let's check the chain with this connections:
    ({1,2},{2,3},{3,4},{4,5},{4,6},{6,5})
    The optimal solution here would be to break 3 rings, making 3 full and
    separate rings. So the result is 3.

    Input: Information about the connected rings as a tuple of sets with
    integers.

    Output: The number of rings to break as an integer.
'''

'''                                 == RU ==
    Кузнец дал своему ученику задание, приказав сделать набор колец. Ученик не
    был специалистом в этом деле и в результате некоторые кольца (если честно,
    большинство) получились соединенными вместе. Теперь он просит помочь ему
    разделить кольца и найти количество колец, которое необходимо сломать, чтобы
    освободилось наибольшее число колец.

    Все кольца пронумерованы, и как было сказано соединены. Эта информация
    представлена как последовательность множеств. Каждое множество описывает
    соединенные кольца. Например: {1, 2} означает, что 1ое и 2е кольца
    соединены. Вы должны посчитать, сколько колец мы должны сломать, чтобы
    получить максимальное число разделенных колец. Каждое из колец пронумеровано
    в диапазоне от 1 до N, где N является общим числом колец.

    Вот пример цепи со следующими связями:
    ({1,2},{2,3},{3,4},{4,5},{4,6},{6,5}).
    Оптимальным решением здесь будет разбить 3 кольца, получив 3 целых и
    отдельных кольца. Таким образом ответ 3.

    Входные данные: Информация о связанных кольцах в виде кортежа множеств с
    целыми числами.

    Выходные данные: Количество разорванных колец, как целое.
'''

class Breaker:
    def __init__(self, rings):
        self.rings = list(rings)

    def breakOne(self, key, rings):
        ''' Delete one ring from all connections '''
        for i, pair in enumerate(rings):
            rings[i] = pair - {key}
        return rings

    def are_separate(self, rings):
        ''' Check if all rings are separate '''
        for pair in rings:
            if len(pair) > 1: return False
        return True

    def solution(self):
        ''' Find minimum number of rings to be broken to release the others '''
        from itertools import combinations

        options = []
        total = max(max(r) for r in self.rings)

        for maxtobreak in range(1, total):
            for option in combinations(range(1, total + 1), maxtobreak):
                rings = self.rings[:]
                broken = 0

                for ring in option:
                    rings = self.breakOne(ring, rings)
                    broken += 1
                    if self.are_separate(rings):
                        options.append(broken)
                        break

                if options: return min(options)



def break_rings(rings):
    return Breaker(rings).solution()


if __name__ == '__main__':
    # These "asserts" using only for self-checking and not necessary for auto-testing
    assert break_rings(({1, 2}, {2, 3}, {3, 4}, {4, 5}, {5, 6}, {4, 6})) == 3, "example"
    assert break_rings(({1, 2}, {1, 3}, {1, 4}, {2, 3}, {2, 4}, {3, 4})) == 3, "All to all"
    assert break_rings(({5, 6}, {4, 5}, {3, 4}, {3, 2}, {2, 1}, {1, 6})) == 3, "Chain"
    assert break_rings(({8, 9}, {1, 9}, {1, 2}, {2, 3}, {3, 4}, {4, 5}, {5, 6},
            {6, 7}, {8, 7})) == 5, "Long chain"
    assert break_rings(({3,4},{1,6},{1,2},{9,5},{2,5},{9,2},{8,3},{2,4},{8,4},
            {1,3},{8,1},{1,7},{6,7},)) == 6, "Crash a lot"
    assert break_rings(({1,9},{1,2},{8,5},{4,6},{5,6},{8,1},{3,4},{2,6},{9,6},
            {8,4},{8,3},{5,7},{9,7},{2,3},{1,7},)) == 5, "Best solution"

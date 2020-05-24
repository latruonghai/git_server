s = []

for _ in range(3):
    s.append(list(map(int, input().rstrip().split())))


def formingMagicSquares(list1):
    totals = []
    a = [[[8, 1, 6], [3, 5, 7], [4, 9, 2]],
         [[6, 1, 8], [7, 5, 3], [2, 9, 4]],
         [[4, 9, 2], [3, 5, 7], [8, 1, 6]],
         [[2, 9, 4], [7, 5, 3], [6, 1, 8]],
         [[8, 3, 4], [1, 5, 9], [6, 7, 2]],
         [[4, 3, 8], [9, 5, 1], [2, 7, 6]],
         [[6, 7, 2], [1, 5, 9], [8, 3, 4]],
         [[2, 7, 6], [9, 5, 1], [4, 3, 8]]]
    for p in a:
        total = 0
        for i_pow, j_pow in zip(list1, p):
            for i, j in zip(i_pow, j_pow):
                if not i == j:
                    total += abs(i-j)
        totals.append(total)
    return min(totals)


result = formingMagicSquares(s)
print(result)

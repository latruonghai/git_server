st = input().split()

s = int(st[0])

t = int(st[1])

ab = input().split()

a = int(ab[0])

b = int(ab[1])

mn = input().split()

m = int(mn[0])

n = int(mn[1])

apples = list(map(int, input().rstrip().split()))

oranges = list(map(int, input().rstrip().split()))


def countApplesAndOranges(s, t, a, b, apples, oranges):
    apple = [i for i in apples if s <= a+i <= t]
    orange = [j for j in oranges if s <= b+j <= t]
    print('{}\n{}'.format(len(apple), len(orange)))


countApplesAndOranges(s, t, a, b, apples, oranges)

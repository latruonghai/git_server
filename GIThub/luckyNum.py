n = int (input())
d = []
for i in range(n):
    m = int(input())
    a = list(map(int,input().split()))
    b = sum(a)/m
    b = int(b) if int(b)==b else int(b)+1
    d.append(b)
for i in d:
    print(i)

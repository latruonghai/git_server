def sockMerchant(n, ar):
    c = set(ar)
    countA = 0
    b = [0 for _ in range(len(c))]
    for i in range(len(c)):
        b[i]+=ar.count(c[i])/2
    for j in b:
        if int(j)==j:
            countA+=j
    return countA
n = int(input())

ar = list(map(int, input().rstrip().split()))
print(sockMerchant(n,ar))
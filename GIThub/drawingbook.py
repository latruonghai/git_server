first_multiple_input = input().rstrip().split()

n = int(first_multiple_input[0])

k = int(first_multiple_input[1])

s = list(map(int, input().rstrip().split()))


def nonDivisibleSubset(k, s):
    c = []
    count = [0]*k
    for num in s:
        count[num % k] += 1
    i = 0
    print(count)


nonDivisibleSubset(k, s)

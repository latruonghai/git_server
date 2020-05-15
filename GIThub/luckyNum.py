def isPrime(n):
    for i in range(2,int(n**0.5)+1):
        if n%i==0:
            return False
    return True
n = int(input())
dem =0
temp = n+1
while dem<2:
    for i in range(temp-1,1,-1):
        if isPrime(i):
            temp =i
            dem+=1
            break
print(temp)
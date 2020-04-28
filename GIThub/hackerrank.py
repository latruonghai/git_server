ar_count = int(input())

ar = list(map(int, input().rstrip().split()))

def birthdayCakeCandle(arr):
    max = arr[0]
    dem =1
    for i in range(1,len(arr)):
        if arr[i]==max:
            dem +=1
        elif arr[i]>max:
            dem=1
            max = arr[i]
    return dem
print(birthdayCakeCandle(ar))    
        
    
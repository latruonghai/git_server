c = list(map(int,input().split()))
n=c[0]
m = c[1]
dem = 0
def sumMany(start,end):
    sum = ((end-start+1)*(end+start))/2
    return int(sum)
if n>m:
    tmp1=m-n
    n-=1
    m-=2
    dem+=sumMany(1,m)+sumMany(tmp1,n)
else:
    tmp1=m-n
    n-=1
    m-=2
    dem+=sumMany(1,n)+sumMany(tmp1,m)
    
print (dem)
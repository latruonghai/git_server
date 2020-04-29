n = int(input())

i_startJ_start = input().split()

i_start = int(i_startJ_start[0])

j_start = int(i_startJ_start[1])

i_end = int(i_startJ_start[2])

j_end = int(i_startJ_start[3])

def sum(tup,tup1):
    return (tup[0]+tup1[0],tup[1]+tup1[1])
def distances(tup,tup1):
    return((tup[0]-tup1[0])**2+(tup[1]-tup1[1])**2)**0.5
def printShortestPath(n, i_start, j_start, i_end, j_end):
    d = {(-2,-1):'UL',(-2,1):'UR',(0,2):'R',(2,1):'LR',(2,-1):'LL',(0,-2):'L'}
    d1 = [(-2,-1),(2,1),(0,2),(-2,1),(-2,-1),(0,-2)]
    c = []
    start = (i_start,j_start)
    end = (i_end,j_end)
    dis = distances(start,end)
    #d = ((i_start-i_end)**2+(j_start-j_end)**2)**0.5
    while dis>0:
        if (0<=j_start<n and 0<=i_start<n):
            temp = start
            for i in range(len(d1)):
                start =i_start,j_start =sum(temp,d1[i])
                Dist = distances(start,end)
                if Dist <dis:
                    dis =Dist
                    break
            #if i==len(d1)-1:
                #print("impos")
            else: c.append(d[d1[i]]) 
        else:
            break
    if dis ==0:
        print(len(c))
        print(" ".join(c))
    else:
        print("Impossible")
printShortestPath(n,i_start,j_start,i_end,j_end)
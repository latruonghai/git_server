n = int(input())

i_startJ_start = input().split()

i_start = int(i_startJ_start[0])

j_start = int(i_startJ_start[1])

i_end = int(i_startJ_start[2])

j_end = int(i_startJ_start[3])
#matrix2 = []
#for i in range(n):
    #matrix = [' ' for i in range(n)]
    #matrix2.append(matrix)


# print(matrix2)
def sum(tup, tup1):
    return (tup[0] + tup1[0], tup[1] + tup1[1])


def distances(tup, tup1):
    return ((tup[0] - tup1[0]) ** 2 + (tup[1] - tup1[1]) ** 2) ** 0.5


def printShortestPath(n, i_start, j_start, i_end, j_end):
    d = {(-2, -1): 'UL', (-2, 1): 'UR', (0, 2): 'R', (2, 1): 'LR', (2, -1): 'LL', (0, -2): 'L'}
    #d1 = [(-2, -1), (-2, 1), (0, 2), (2, 1), (2, -1), (0, -2)]
    #des = []
    #d2 = []
    c = []
    #matrix2[i_start][j_start] = 'x'
    #matrix2[i_end][j_end] = 'y'
    start = (i_start, j_start)
    end = (i_end, j_end)
    dis = distances(start, end)
    # d = ((i_start-i_end)**2+(j_start-j_end)**2)**0.5
    while dis > 0:
        if (0 <= j_start < n and 0 <= i_start < n):
            temp = start
            if (i_end<i_start and j_end<j_start):       #on the lowright of end
                d2 = [(-2,-1),(0,-2)]                   #UL, L
            elif (i_end>i_start and j_end<j_start):     #on the upright of end
                d2 = [(2, -1),(0, -2)]                   #LL,L 
            elif (i_end<i_start and j_end>j_start):      #on the lowleft of end
                d2 = [(-2, 1),(0, 2)]                    #UR ,R
            elif (i_end>i_start and j_end>j_start):     #on the upleft of end
                d2 = [(2, 1),(0, 2)]                    #R, LR
            elif (i_end>i_start and j_end==j_start):     #on the up-straight of end
                d2 = [(2, -1)]
            elif (i_end<i_start and j_end==j_start):     #on the low-height of end
                d2 = [(-2, -1)]
            elif (i_end==i_start and j_end<j_start):     #on the up-width of end
                d2 = [(0, -2)]
            elif (i_end==i_start and j_end>j_start):     #on the up-width of end    
                d2 = [(0, 2)]
            for i in range(len(d2)):
                start = i_start, j_start = sum(temp, d2[i])
                Dist = distances(start, end)
                if Dist < dis:
                    dis = Dist
                    break
            c.append(d[d2[i]])
            #if (0 <= j_start < n and 0 <= i_start < n):
                #matrix2[i_start][j_start] = str(len(c))
            if dis<=1:
                break
        else:
            break
    #for i in range(len(matrix2)):
        #print(matrix2[i])
    # print(matrix2)
    if dis == 0:
        print(len(c))
        print(" ".join(c))
    else:
        print("Impossible")


printShortestPath(n, i_start, j_start, i_end, j_end)
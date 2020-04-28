n = int(input())

i_startJ_start = input().split()

i_start = int(i_startJ_start[0])

j_start = int(i_startJ_start[1])

i_end = int(i_startJ_start[2])

j_end = int(i_startJ_start[3])
d = {'UL':(2,-1),'UR':(2,1),'R':(0,2),'LR':(-2,1),'LL':(-2,-1),'L':(0,-2)}
def printShortestPath(n, i_start, j_start, i_end, j_end):
    if i_start<i_end or j_start<j_end:
        while(i_start<i_end or j_start<j_end):
            
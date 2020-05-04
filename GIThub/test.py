n = int(input())

scores = list(map(int, input().rstrip().split()))



def breakingRecords(scores):
    mintime = maxtime = 0
    
    minscore = maxscore = scores[0]
    for i in range (1,len(scores)):
        if scores[i]>maxscore:
            maxscore=scores[i]
            maxtime +=1
        if scores[i]<minscore:
            minscore = scores[i]
            mintime +=1
    return [maxtime,mintime]
result = breakingRecords(scores)
c = " ".join(map(str,result))
print(c)
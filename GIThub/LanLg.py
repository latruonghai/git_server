n = input().split()
def isSorted(list):
    s= sorted(list)
    if s ==list:
        return True
    else:
        return False
def stringTrip(list):
    a = []
    if list[0].find('lios')!=-1 or list[0].find('initis')!=-1 or list[0].find('etr')!=-1:
        for i in range (1,len(list)):
            if list[i].find('lios')!=-1:
                a.append((0,0))
            elif list[i].find('etr')!=-1:
                a.append((0,1))
            elif list[i].find('initis')!=-1:
                a.append((0,2))
    elif list[0].find('liala')!=-1 or list[0].find('inites')!=-1 or list[0].find('etra')!=-1:
        for i in range (1,len(list)):
            if list[i].find('liala')!=-1:
                a.append((1,0))
            elif list[i].find('etra')!=-1:
                a.append((1,1))
            elif list[i].find('inites')!=-1:
                a.append((1,2))
    else:
        return 'NO'
    if len(list)-len(a)>1: return 'NO'
    else: return 'YES' if isSorted(a) else 'NO'
print(stringTrip(n))
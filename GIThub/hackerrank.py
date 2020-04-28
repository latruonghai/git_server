s = input()

def timeConverstion(s):
    a = s.rstrip().split(':')
    temp = int(a[0])
    temp1 = a[len(a)-1][2:4]
    if (temp1.upper()=="PM" and temp<12):
        if temp<12:
            temp+=12
            a[0]=str(temp)
    elif (temp1.upper()=="AM" and temp==12):
        a[0]="00"
    a[len(a)-1]=a[len(a)-1].replace(temp1,"")
    return ":".join(a)
print(timeConverstion(s))
    
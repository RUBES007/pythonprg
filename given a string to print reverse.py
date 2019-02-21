p=input().split()
q=[]
for x in p:
    q.append(x[::-1])
for i in range(0,len(q)):
    if(i==len(q)-1):
        print(q[i],end=(""))
    else:
        print(q[i],end=(" "))

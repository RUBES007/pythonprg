o=int(input())
m=0
l=0
while(o>0):
  d=o%10
  o=o//10
  m+=d
p=m
while(m>0):
  i=m%10
  l=l*10+i
  m=m//10
if(p==l):
  print("YES")
else:
  print("NO")

k=input("")
length=int(len(k))
for i in range(0, int(length/2 + 1)):
   if k[i]==k[-i - 1]:
      i+=1
   else:
      break
if i<(length / 2):
   print("NO")
else:
   print("YES")

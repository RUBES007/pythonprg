f1 = 1
f2 = 10
for num in range(f1,f2 + 1):
   if num > 1:
       for i in range(2,num):
           if (num % i) == 0:
               break
       else:
           print(" ",num,end='')

x,y=input().split()
x,y=int(x),int(y)
for num in range(150,160):
	sum=0
	temp=num
	while temp>0:
		value=temp%10
		sum=sum+value**3
		temp=temp//10
	if num==sum:
		print(num,end='\t')

ef hunt_20():
	u=int(input())
	v=int(input())
	r=0
	for i in range(u,v):
		if r!=1:
			r+=1
	print(r)
try:
	hunt_20()
except:
	print('Invalid')

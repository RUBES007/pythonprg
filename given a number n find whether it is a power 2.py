u=int(input())
for i in range(1,u):
	w=2**i
	if w==u:
		print("no")
		break
else:
	print("yes")

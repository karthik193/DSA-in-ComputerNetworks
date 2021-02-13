def destuff(ip):
	print("input:", ip)
	n = len(ip)
	c=0
	op=[]
	for i in range(n):
		if(ip[i] == "1"):
			c+=1
			op.append(ip[i])
		else:
			if(c!=5):
				op.append(ip[i])
			c=0

	op = "".join(op)
	ans = "110101111101011111101011111110"
	if(ans == op):
		print("destuffed: ",op)
	

if __name__ == '__main__':
	ip = "110101111100101111101010111110110"
	destuff(ip)

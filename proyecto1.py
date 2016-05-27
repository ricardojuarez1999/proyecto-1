def prob_1(n):
	return n %2 == 0
def prob_2(n):
	return (n-32)/1.8
def prob_3(b,p):
	b1 = b
	for i in range(1,p):
		b = b*b1
	return b
def prob_4(a,c):
	izq = (c-len(a))//2
	der = c - (izq+len(a))
	return (("*"*izq)+ a +("*"*der))
def prob_5(x0,x1,x2,y0,y1,y2):
	lis1=[]
	lis2=[]
	lis1.append(x0)
	lis1.append(x1)
	lis1.append(x2)
	lis2.append(y0)
	lis2.append(y1)
	lis2.append(y2)
	wx = (lis1[1]*lis2[2])-(lis1[2]*lis2[1])
	wy = (lis1[2]*lis2[0])-(lis1[0]*lis2[2])
	wz = (lis1[0]*lis2[1])-(lis1[1]*lis2[0])
	return [wx, wy,wz]
def prob_6():
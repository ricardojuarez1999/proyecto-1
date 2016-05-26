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
	letras = a
	le = float(len(letras))
	an = "* "
	re = an*((c/2.0)-le)
	return (re+a+re) 
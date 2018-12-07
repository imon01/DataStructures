"""
	Discrete problems:

	Catalan functions:
		counting number of possible binary trees
"""


def catalan_API(n):
	print("Calling Catalan")
	k = catalan(n)
		
	print("Catalan( " +str(n) +" ) = " +str(k))

	kk = catalan_recursion(n)
	print("Catalan( " +str(n) +" ) = " +str(kk) + "\trecursion")

	k_slick = catalan_slick(n)
	print("Catalan_slick( " +str(n) +" ) = " +str(k_slick) + "\tslick")



def catalan_recursion(n):

	if n <=1:
		return 1

	k = 0
	for i in range(0, n):
		k +=catalan(i)*catalan( n-i-1)

	return k


def catalan(n):
	
	if n < 2:
		return 1
	T_table = { 0: 1, 1: 1}
	t_n = 0	
	n_ = 2
	n+=1
	i = 0
	while( n_ != n):		

		i = 0 
		t_n = 0
		while(i < n_):		
			t_n += T_table[i]*T_table[n_- i-1]
			i+=1

		if n_ not in T_table:
			T_table.setdefault(n_, t_n)
		n_+=1
	
	return T_table[n-1]	

def catalan_slick(n):
	# C_n = 2(2n-1)/(n+1) * C_n-1

	if n < 2:
		return 1
	c = 1
	n_  = 2
	n+=1

	while n_ != n:
		c *= ( 4*n_ - 2)/(n_+1)
		n_+=1

	return int(c)


def catalan_aux(n):
	pass

def main():

	for i in range(0, 7):
		catalan_API(i)	

if __name__ == "__main__":
	main()

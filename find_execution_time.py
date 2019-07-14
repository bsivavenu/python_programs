from time import time

def one(a,b):
	return a+b

def two(a,b):
	if a >=3 :
		a = a
	if b != a:
		b = a-1
	return a+b

if __name__ == "__main__":
	init = time()
	for i in range(0,1000000):
		one(2,1)
	print('one time:',time()-init )
	init = time()
	for i in range(0,1000000):
		two(3, 5)
	print('two time:',time()-init )



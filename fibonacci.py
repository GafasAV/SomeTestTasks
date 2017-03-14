def fib(n):
	if n == 0:
		return 0
	elif n == 1:
		return 1
	else:
		return fib(n - 1) + fib(n - 2)
    
if __name__ == "__main__":
	n = int(input("Input fibonacci range :"))
	
	for i in range(1, n+1):
		print("{0} step = {1}".format(i, fb.fib(i)))

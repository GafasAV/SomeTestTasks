def fact(n):
	if n == 0 or n == 1:
		return 1
	else:
		return n * fact(n - 1)

if __name__ == "__main__":
	
	count = int(input("Input iteration count :"))
	
	result = fact(count)
	print(result)

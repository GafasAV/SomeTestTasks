def fizzBuzz(n):
	
	if n % 3 == 0 and n % 5 == 0:
		return "FizzBuzz"
	elif n % 3 == 0:
		return "Fizz"
	elif n % 5 == 0:
		return "Buzz"
	else:
		return str(n)
		

if __name__ == "__main__":
	
	count = int(input("Input numbers count :"))
	result = ""
	
	print(result.join(fizzBuzz(n) for n in range(1, count+1)))

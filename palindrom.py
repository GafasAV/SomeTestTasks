def isPalindrom(str):
	revstr = str.lower()[::-1]
	
	print("string {0}".format(str))
	print("rev_st {0}".format(revstr))
	
	return str == revstr
  
if __name__ == "__main__":	
	
	str = str(input("Input string for checking :"))

	result = isPalindrom(str)
	print(result)

#python implementation of fizzbuzz
#!/usr/local/bin/python

def fizzbuzz(max = 100):
	"""
	takes in an integer value (default 100) and prints a list, 
	if the number is evenly divisible by 3 then it prints Fizz, otherwise it prints Buzz
	"""
	for i in range(1,max):
		Final = str(i) + " "
		if i%3 == 0: Final += "Fizz"
		if i%5 == 0: Final += "Buzz"
		print Final
	return True

if __name__ == "__main__":
	"""
	run fizzbuzz to 100
	"""

	fizzbuzz()

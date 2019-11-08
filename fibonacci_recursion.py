# A fibonacci series is a number series 
# where the number is a sum of two previous 
# numbers 

def fib(num):
	"""
	In this we will take value of number and print the value
	we will use recursion to call the function 
	"""

	if num == 0:
		return 0

	elif num == 1:
		return 1

	else:
		return fib(num - 1) + fib(num - 2)


# Input of the element 
number_of_elements = int(input("Enter the number of elements in fibonacci series :"))
print("Entered value is ", number_of_elements)
# looping through the range
for num in range(number_of_elements):
	print(fib(num))
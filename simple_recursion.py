#In this I will be coding a simple recursion to print list 
# of elements 


def list_elements(num):
	"""
	Recursively print all the elements 
	using recursion
	"""
	#Condition when the function has to 
	#return
	if num <= 1:
		print(num)
		return

	#Recursively calling the function
	list_elements(num-1)
	# printing the element after  coming out of function
	print(num)

list_elements(10)
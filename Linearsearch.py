# In this code we will do a linear search of an array
# the time complexity is O(n)

X = [10,4,5,24,6,1,3, 7, 11, 2, 1]

#look for an element to see if it is present are not

def linear_search(check_value, X):
	element_present = False
	for i in X:
		if i == check_value:
			print("The %s is present in array" % check_value)
			element_present = True
			break
	if not element_present:
		print("The %s is not present" % check_value)


linear_search(1,X)
linear_search(8,X)

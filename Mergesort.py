# Merge sort . This is one of the efficient algorithms 
# O(nlogn) complexity

X = [10,4,5,24,6,1,3, 7, 11, 2, 1]

#In merge sort break the nodes into an array of elements 

# We use concept of recursion here 
def mergesort(x):
	if len(x) > 1:	
		#The first task is to break the array into two

		# find the mid point 

		midpoint = round(len(x)/2)

		right_array = x[:(midpoint)]
		left_array  = x[(midpoint):]
	 
		print(right_array)
		print(left_array)
		# iteratively calling the function again

		mergesort(right_array)
		mergesort(left_array)


		# now we will be having the arrays

		i = j = k = 0

        # copy arrays into temporary variables

		while i < len(left_array) and j < len(right_array):
			if left_array[i] < right_array[j]:
				x[k] = left_array[i]
				i+=1
			else:
				x[k] = right_array[j]
				j+=1
			k+=1

        # checking for left out elements
		while i < len(left_array):
			x[k] = left_array[i]
			i+=1
			k+=1
		while j < len(right_array):
			x[k] = right_array[j]
			j+=1
			k+=1
	return x        


print(mergesort(X))
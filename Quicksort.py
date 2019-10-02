#Implement quicksort to sort the below elements 
#In this we have to pick a pivot element and 

X = [10,4,5,24,6,1,3, 7, 11, 2, 1]

#It will take the pivot of array and places 
# the elements below the value in left and places 
# the values above in right pivot

def partition(arr, low, high):
	
	#Get the variable pointing to lowest index
	i = low -1

	# Get the pivot element
	pivot = arr[high]

	# Now iterating through the loop of remaining array 
	# in left side
	for j in range(low, high):
		# Checking condition if arr[i] < arr[]
		if arr[j] <= pivot:
			# update the lower index
			i+=1
			# Swap the index with array
			arr[i],arr[j] = arr[j], arr[i]

	#condition to swap the pivot		
	arr[i+1],arr[high] = arr[high],arr[i+1] 

    # Returning the current pivot position from which 
    # the left sub array and right sub array will further
    # continue the sort
	return (i+1)


def Quicksort(arr, low, high):
	if low < high:
		pi = partition(arr,low,high)

		# Sort the left side of array	
		Quicksort(arr, low, pi-1)

		# Sort the right side of array
		Quicksort(arr,pi+1, high)



n = len(X)

Quicksort(X,0,n-1)

print(X)
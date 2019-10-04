# In this we will implement binary search to find whether an element 
# is present in a given array. We will basically consider the element to be sorted 
# before doing it 


input_array = [1,2,3,5,8,10,12,14,18,20,21,120]
def mid_point_value(low, upper):
	return int(low + (upper - low)/2)


def binary_search(check_value, input_array):
	#In this we will find the middle element and successively look for the element

	value_found = False
	low = 1
	upper = len(input_array)
	mid_point = mid_point_value(low,upper)
	while not value_found:

		#if the mid value is more than the check_value
		if input_array[mid_point] > check_value:
			# we must look inside the lower bound
			print("The mid value is greater than check_value")
			upper = mid_point -1

		elif input_array[mid_point] < check_value:
			# we must look inside the upper bound
			low = mid_point + 1

		elif input_array[mid_point] == check_value:
			# The value is matching the array
			print("The %s is found in the given array " % check_value)
			value_found = True
			break
		# If you have elif over here  you may end up in continous loop

		if low >= upper:
			value_found = True
			print("The %s is not present" % check_value)
			break
		print("lower: %s " % low)
		print("upper: %s" % upper)
		mid_point = mid_point_value(low, upper)

binary_search(1,input_array)
binary_search(15, input_array)
binary_search(150, input_array)
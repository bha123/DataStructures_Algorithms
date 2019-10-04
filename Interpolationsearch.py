# Interpolation search
# midpoint = Low + ((High - Low)/(A[low] - A[High]))*( Searched_term - A[low])
# While Search_value_found is False:
#      if Low > High or A[high] == A[low]:
#           print("Item not found")
#           exit
#      if A[mid] == Search_value_found:
#			print("Value found")
#	   elif A[mid] < target_value:
# 			mid = low + 1
#      elif A[mid] > target_value:
#			mid = high - 1

input_array = [1,2,3,5,8,10,12,14,18,20,21,120]

def get_midpoint(low, high, search_value, input_array):
	return low + ((high - low)/(input_array[high] - input_array[low]))*(search_value - input_array[low])

def Interpolation(search_value, input_array):
	
	low = 0
	high = len(input_array) - 1
	Search_value_found = False
	while  not Search_value_found:
		print("low : {} , high : {}, comparision : {}".format(low, high, low > high))
		
		if low > high or input_array[low] == input_array[high] :
			print("The %s is not present" % search_value)
			Search_value_found = True
			break
		midpoint =int( get_midpoint(low, high, search_value, input_array))

		if input_array[midpoint] > search_value:
			high = midpoint - 1
		elif input_array[midpoint] < search_value:
			low = midpoint + 1

		elif input_array[midpoint] == search_value:
			print("The %s value is present" % search_value)
			Search_value_found = True
			break

Interpolation(10, input_array)
Interpolation(121, input_array)
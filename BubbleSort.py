# Simple bubble sort algorithm
# In this we will swap the elements adjenct to each other  of an array until they come in
# order
# @ nmania03@gmail.com

#Given array 

X = [10,4,5,24,6,1,3, 7, 11, 2, 1]
m = len(X)
sorted_array = False
while not sorted_array:
	sorted_array = True
	for i in range(m):
		for j in range(m-i-1):			
			if(X[i] > X[i+1]):
				X[i+1],X[i] = X[i],X[i+1]
				sorted_array = False

for i in X:
	print(i)
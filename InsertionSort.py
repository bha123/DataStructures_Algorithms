# Insertion Sort in order to arrange elements

X = [10,4,5,24,6,1,3, 7, 11, 2, 1]
m = len(X)
sorted_array = False
for i in range(1,m):

	# you have to target element above the present one
    
    key = X[i]
    j = i -1
    
    # looping through it and changing the position until you get them sorted
    while j >=0 and  key < X[j] :
    	X[j+1] = X[j]
    	j-=1
    X[j+1] = key

	
print(X)


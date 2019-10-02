# Selection sort will reference to pick the element and
# Swap it with the element that is least and do it till the end of an array
# then move one position left


#X = [10,4,5,24,6,1,3, 7, 11, 2, 1]
X = [14,33,27,10,35,19,42,44]

for i in range(0, len(X)-1):

	# check the rest of the list in while loop
	# to see whether there is any small value 
	# if so then swap it and continue the loop
    
    # Start comparing from next element
	j = i + 1
	while j < len(X):
		if X[i] > X[j]:
			X[i] ,X[j] = X[j], X[i]
		j+=1
	print(X)	




print(X)


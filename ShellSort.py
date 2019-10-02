# Implement shell sort which is a variation in insertion sort where 
# the sort will do among elements at far ends
#

#X = [10,4,5,24,6,1,3, 7, 11, 2, 1]
X= [35,33,42,10,14,19,27,44]

# first let us create a gap and loop through the elements 

def shell_sort(x):

	#  caliculate the Gap between the elements 
	# knuth formula 
	
	gap = len(x)//2

	#print(gap)
	while gap > 0:

		j = 0
		for i in range(gap, len(x)):
			print(x)
			if x[j] > x[i]:
				x[j],x[i] = x[i],x[j]
			j+=1
		
		gap//=2
		print("Gap getting updated to %s" % gap)
	#print(x)	
shell_sort(X)
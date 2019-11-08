# Tower of hanoi is a classic programming problem
# in this you will have three poles and you have to move 
# discs from one side to other while the condition is 
# larget disk will not sit on top of smaller disk

#      |              |            |
#      |              |            |
#	 ###### 	      |            |
#   ########        #####         ### 
#   ---------     ---------    ----------
#   From pole     Mid pole       To Pole   

# The trick here is if you have odd number of pole you have 
# to move top disk to To pole and Mid pole in case if it is 
# even

def tower_of_hanoi(number_of_disks, from_pole, mid_pole, to_pole):
	"""
	The function takes values of number of disks
	The poles are presented with Characters 'A', 'B', and 'C'
	The function returns the list of steps to be followed in order 
	to transfer from "From pole " to "To pole"
	"""

	if (number_of_disks == 1):
		print("Move disks from {0} to {1}".format(from_pole, to_pole))
		return

	# switching mid_pole and to_pole	
	tower_of_hanoi(number_of_disks - 1, from_pole, to_pole, mid_pole)

	print("Move disks from {0} to {1}".format(from_pole, to_pole))

	#switching from_pole and mid_pole positions 
	tower_of_hanoi(number_of_disks - 1, mid_pole, from_pole, to_pole)


tower_of_hanoi(3,'A','B','C')	


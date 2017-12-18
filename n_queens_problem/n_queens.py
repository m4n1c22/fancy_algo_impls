arr = []

def is_unique_entry(t_arr):
	count = 0
	for i in range(0, len(t_arr)):
		if t_arr[i] == 1:
			count++
	if count > 1:
		return False
	else:
		return True
		

def is_collision():
	#check rook straights
	#row wise check
	k = -1
	for i in range(0, len(arr)):
		k = (k+1)%len(arr)
		for j in range(0, len(arr)):
			if k != j and arr[i][k] != None and arr[i][k] == arr[i][j]:
				return False
	#column wise check
	k = -1		
	for i in range(0, len(arr)):
		k = (k+1)%len(arr)
		for j in range(0, len(arr)):
			if k != j and arr[k][i] != None and arr[k][i] == arr[j][i]:
				return False
	#check bishop diagonals
#	for i in range(0, len(arr)):
#		for j in range(0, len(arr)):
			
			


	return True

def backtrack_function(x):
	if x == 0:
		return True
	for i in range(0, len(arr)):
		for j in range(0, len(arr)):
			if arr[i][j] == None:
				arr[i][j] = 1
			if is_collision() == False:
				if backtrack_function(x-1)==True:
					return True
	return False
								
def display_arr():
	print ("Solution: ")
	for v in arr:
		print (v)

if __name__ == '__main__':

	n = int(raw_input("Enter a value of n for n queens problem: "))
	del arr[:]
	arr = [[None]*n for _ in range(n)]
	
	arr[0][0] = 1
	arr[1][2] = 1
	print (is_collision())
	display_arr()
	#if backtrack_function(n) == True:
	#	display_arr()
	#else:
#		print ("No solution")

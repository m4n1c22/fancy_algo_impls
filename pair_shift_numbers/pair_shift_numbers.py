arr = []

def backtrack_function(x):
	if x==0:
		return True
	for i in range(0, len(arr)):
		if i+x+1 == len(arr):
			return False
		if arr[i] == None and arr[i+x+1] == None:
			arr[i] = x
			arr[i+x+1] = x
			ret_val = backtrack_function(x-1)
			if ret_val == False:
				arr[i] = None
				arr[i+x+1] = None
			else:
				return ret_val
	return False

def display_arr():
	print ("Solution: ")
	print (arr)

if __name__ == '__main__':

	n = int(raw_input("Enter a value of n to generate pairshift numbers: "))
	del arr[:]
	arr = [None]*2*n
	if backtrack_function(n) == True:
		display_arr()
	else:
		print ("No solution")
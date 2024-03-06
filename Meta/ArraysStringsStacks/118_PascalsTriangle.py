def generate(numRows):
	arr = [[1 if (j==0 or j == i) else 0 for j in range(i+1)] for i in range(numRows)]
	for i in range(2,numRows):
		for j in range(i+1):
			if j != 0 and j!=i:
				arr[i][j] = arr[i-1][j-1]+ arr[i-1][j]
	return arr

numRows = 5
print(generate(numRows))
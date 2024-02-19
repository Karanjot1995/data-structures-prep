def rotate(matrix):
  n = len(matrix)

  #transpose
  for i in range(n):
    for j in range(i,n):
      matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
      
  #reverse rows
  for i in range(n):
    for j in range(n//2):
      k = n-j-1
      matrix[i][j], matrix[i][k] = matrix[i][k], matrix[i][j]
  return matrix

# def rotate(matrix):
#   n = len(matrix)
#   s = []
#   for i in range(n-1,-1,-1):
#     for j in range(n):
#       s.append(matrix[i][j])
#   ptr = 0
#   for i in range(n):
#     ptr = i
#     for j in range(n):
#       matrix[i][j] = s[ptr]
#       ptr+=n

print(rotate([[1,2,3],[4,5,6],[7,8,9]]))
# 1  2  3             
# 4  5  6
# 7  8  9

# Transpose
# 1  4  7
# 2  5  8
# 3  6  9

# Reverse rows
# 7  4  1
# 8  5  2
# 9  6  3

#op = [[7, 4, 1], [8, 5, 2], [9, 6, 3]]

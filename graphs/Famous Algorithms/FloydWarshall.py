from Templates.UndirectedWeighted import Graph
from queue import PriorityQueue

class Graph():

  def floydWarshall(self,matrix,):
    n = len(matrix)
    for i in range(n):
      for j in range(n):
        if matrix[i][j]==-1:
          matrix[i][j]=float('inf')
        if i == j: matrix[i][j] = 0
   
    for k in range(n):
      for i in range(n):
        for j in range(n):
          matrix[i][j] = min(matrix[i][j], (matrix[i][k]+matrix[k][j]))

    for i in range(n):
      for j in range(n):
        if matrix[i][j]==float('inf'):
          matrix[i][j]= -1

    return matrix

g = Graph()
arr=  [[0,25], [-1,0]]
print(g.floydWarshall(arr))


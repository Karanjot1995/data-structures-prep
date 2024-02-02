# class Solution:
#     def findCircleNum(self, mat) -> int:
#         def bfs(i,adj,visited):
#             queue = []
#             queue.append(i)
#             visited[i] = True
            
#             while queue:
#                 i = queue.pop(0)
#                 for j in range(n):
#                     if adj[i][j] == 1 and not visited[j]:
#                         visited[j] = True
#                         queue.append(j)
#         n = len(mat)
#         provinces = 0
#         visited = [False]*n
#         for i in range(n):
#             if not visited[i]:
#                 provinces += 1
#                 bfs(i,mat,visited)
#         return provinces

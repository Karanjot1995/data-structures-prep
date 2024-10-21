# from Templates.DirectedWeighted import Graph

# class Graph(Graph):
    
#     def topo(self):
#       graph = self.adj
#       vis = [0]*len(graph)
#       s=[]
#       #node[0] is the node and node[1] is the weight
#       def dfs(curr):
#         vis[curr] = 1
#         for neighbor in graph[curr]:
#           if not vis[neighbor[0]]:
#             dfs(neighbor[0])
#         s.append(curr)

#       for node in graph:
#         if not vis[node]:
#           dfs(node)
          
#       return s
    
#     def shortestPathDAG(self):
#       adj = self.adj
#       s = self.topo()
#       print(s)
#       print(adj)
#       dist = [float('inf')]*len(s)
#       dist[-1]=0
#       while s:
#         u = s.pop()
#         for neighbor in adj[u]:
#           v = neighbor[0]
#           wt = neighbor[1]
#           if dist[u]+wt<dist[v]:
#             dist[v]=dist[u]+wt
#       return dist
        




# g = Graph(6)

# g.addVertex(0)
# g.addVertex(1)
# g.addVertex(2)
# g.addVertex(3)
# g.addVertex(4)
# g.addVertex(5)
# g.addVertex(6)

# g.addEdge(0, 1, 2)
# g.addEdge(1, 3, 1)
# g.addEdge(2, 3, 3)
# g.addEdge(4, 0, 3)
# g.addEdge(4, 2, 1)
# g.addEdge(5, 4, 1)
# g.addEdge(6, 4, 2)
# g.addEdge(6, 5, 3)


# print(g.shortestPathDAG())


def countOfPalinder(str, queries):
    n = len(str)
    is_palindrome = [[False for j in range(n)] for i in range(n)]

    for i in range(n):
        is_palindrome[i][i] = True
        if i+1<n and str[i+1] == str[i]:
          is_palindrome[i + 1][i] = True

    for i in range(n-1,-1,-1):
        for j in range(i + 1, n):
            if str[i] == str[j]:
                is_palindrome[i][j] = is_palindrome[i + 1][j - 1]
            else:
                is_palindrome[i][j] = False

    print(is_palindrome)

    ans = []
    for l, r in queries:
        res = 0
        for i in range(l, r + 1):
            for j in range(i, r + 1):
                if is_palindrome[i][j]:
                    res += 1
        
        ans.append(res)

    return ans


print(countOfPalinder("xabccba", [[0,6]]))
# Alien Dictionary
#dict = {"baa","abcd","abca","cab","cad"}
def findOrder(alien_dict, N, K):
  adj=[[] for _ in range(K)]
  # in_degree = [0]*K

  for i in range(N-1):
    s1,s2 = alien_dict[i], alien_dict[i+1]
    l = min(len(s1), len(s2))
    for j in range(l):
      if s1[j]!=s2[j]:
        n1,n2 = ord(s1[j]) - 97,ord(s2[j]) - 97 
        adj[n1].append(n2)
        # in_degree[n2]+=1
        break

  def topo_sort(graph):
    in_degree=[0]*K
    for i in range(K):
      for j in adj[i]:
        in_degree[j]+=1
    print(in_degree)
    
    q=list()
    topo_sort = []
    for i in range(K):
      if in_degree[i]==0:
        q.append(i)

    while q:
      curr = q.pop(0)
      topo_sort.append(curr)
      for neighbor in graph[curr]:
        in_degree[neighbor]-=1
        if in_degree[neighbor]==0:
          q.append(neighbor)

    return topo_sort
  
  topo=topo_sort(adj)
  
  ans=list()
  for i in topo:
      ans.append(chr(97+i))
  return ans

print(findOrder(["baa","abcd","abca","cab","cad"],5,4))


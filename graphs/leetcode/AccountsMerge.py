from Templates.DisjointSet import DisjointSet

def accountsMerge(accounts):
  V = len(accounts)
  ds = DisjointSet(V)
  mapMailNode = {}

  #connecting nodes and making ultimate parent
  for i in range(V):
    for j in range(1,len(accounts[i])):
      mail = accounts[i][j]
      if mail not in  mapMailNode:
        mapMailNode[mail] = i
      else:
        #if mail is already found on some other index 
        # then make that index the parent of this index
        ds.unionByRank(mapMailNode[mail],i)
  print(mapMailNode)


  #merging mails according to their ultimate parents
  mergeMail = [[] for i in range(V)]
  for mail in mapMailNode:
    i = mapMailNode[mail]
    up_i = ds.findUParent(i)
    mergeMail[up_i].append(mail)


  ans = []
  for i in range(V):
    mergeMail[i].sort()
    if len(mergeMail[i]):
      name = accounts[i][0]
      mergeMail[i].insert(0, name)
      ans.append(mergeMail[i])

  return ans

accounts = [["John","johnsmith@mail.com","john_newyork@mail.com"],["John","johnsmith@mail.com","john00@mail.com"],["Mary","mary@mail.com"],["John","johnnybravo@mail.com"]]
print(accountsMerge(accounts))
#OP = [["John","john00@mail.com","john_newyork@mail.com","johnsmith@mail.com"],["Mary","mary@mail.com"],["John","johnnybravo@mail.com"]]

# mailMapNode = {
# 'johnsmith@mail.com': 0, 
# 'john_newyork@mail.com': 0, 
# 'john00@mail.com': 1, => this will have the ultimate parent 0 as its neighbor was connected to 0 
# 'mary@mail.com': 2, 
# 'johnnybravo@mail.com': 3}
      
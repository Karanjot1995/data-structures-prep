'''
Goldman Sachs | Coderpad | Find the largest tree - https://leetcode.com/discuss/interview-question/1837497/goldman-sachs-coderpad-find-the-largest-tree

== Instructions ==

Given a forest (one or more disconnected trees), find the root of largest tree and return its Id. If there are multiple such roots, return the smallest Id of them.

Complete the largestTree function in the editor below.
It has one parameter, immediateParent, which is a map containing key-value pair indicating child -> parent relationship. The key is child and value is the corresponding immediate parent.

Constraints
- Child cannot have more than one immediate parent
- Parent can have more than one immediate child
- The given key-value pair formes a well-forest (a tree of n nodes will have n-1 edges)

Example:

Input: { {1 -> 2}, {3 -> 4} }

Expected output: 2

Explanation: There are two trees one having root of Id 2 and another having root of Id 4.
Both trees have size 2. The smaller number of 2 and 4 is 2. Hence the answer is 2.
'''

from collections import defaultdict

def get_tree_size(parent_child_map, root):
    ans = 0
    stack = [root]
    print(parent_child_map)
    while stack:
        ans += 1
        node = stack.pop()
        print(node)
        
        if node in parent_child_map:
            for child in parent_child_map[node]:
                stack.append(child)
    return ans

def get_tree_size_recursive(parent_child_map, root):
    if root not in parent_child_map:
        return 1

    ans = 0
    for child in parent_child_map[root]:
        ans += get_tree_size(parent_child_map, child)
    
    return ans + 1

# GRAPH - O(V + E)
# TC - O(RK + len(dict)) | SC - O(N) for stack where N is the total number of nodes
def largestTree(immediateParent):
    roots = set()
    parent_child_map = defaultdict(list) # parent: [child1, child2, ...]
    max_tree_size = min_root = 0

    # O(len(dict))
    for child, parent in immediateParent.items():
        parent_child_map[parent].append(child)
        
        # if its a root i.e. it does not have any parent
        if parent not in immediateParent:
            roots.add(parent)
    
    # O(R) where R is the num of unique roots
    print(roots)
    for root in roots:
        # O(k) where k is max number of nodes in any tree this can be all the nodes for skewed tree
        cur_tree_size = get_tree_size(parent_child_map, root)
        
        if cur_tree_size > max_tree_size:
            max_tree_size = cur_tree_size
            min_root = root
        elif cur_tree_size == max_tree_size:
            min_root = min(min_root, root)
    return min_root

# Example -> op: 2
print(largestTree({ 1: 2, 3: 4 }))

# Two trees of same size -> op: 3
print(largestTree({ 9: 4, 1: 4, 5: 2, 8: 4, 7: 3, 2: 3, 6: 7, 10: 4 }))
#4,9,8,1,10     3,7,6,2,5         

# More than two trees -> op: 15
print(largestTree({ 2: 3, 7: 8, 12: 15, 3: 1, 13: 15, 11: 15, 9: 8, 5: 12}))

# Tree size differ by one -> op: 23
print(largestTree({ 35: 33, 33: 28, 31: 22, 28: 25, 34: 31, 29: 27, 21: 23, 25: 21, 22: 29}))

# Really large index values -> op: 300000000
print(largestTree({
        200000000: 300000000,
        500000000: 200000000,
        700000000: 300000000,
        600000000: 700000000,
        900000000: 400000000,
        100000000: 400000000,
        800000000: 400000000,
        1000000000: 400000000,
    }
))

# USING DFS maybe? - https://www.geeksforgeeks.org/size-of-the-largest-trees-in-a-forest-formed-by-the-given-graph/










def largestTree(adj, V):
     
    visited = defaultdict(bool)
    for parent in adj:
      visited[parent]= False
      for node in adj[parent]:
        visited[node] = False
    
    print(visited)
    answer = 0

    def dfs(u):
      visited[u] = True
      sz = 1
      # print(visited,adj)
      print(u)
      for i in range(0, len(adj[u])):
          if (visited[adj[u][i]] == False):
              # Perform DFS if the node is not yet visited
              sz += dfs(adj[u][i])
      return sz
  
    # Iterating through all the vertices

    for node in adj:
      # print(node)
      if (visited[node] == False): answer = max(answer,dfs(node))
         
    return answer

def createAdj(edges):
  adj = defaultdict(list)

  for node,parent in edges.items():
    adj[parent].append(node)
  return adj   
      

edges = { 35: 33, 33: 28, 31: 22, 28: 25, 34: 31, 29: 27, 21: 23, 25: 21, 22: 29}
# edges = {1:0,2:0,4:3}
adj = createAdj(edges)
# print(adj)
print(largestTree(adj, 12))
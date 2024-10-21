# https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-tree-iii/

"""
# Definition for a Node.
class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        self.parent = None
"""

'''
CLARIFYING QUESTIONS
- Are there duplicates in the tree? (APPROACH 1 won't work for duplicates)
- Will there always be a common ancestor?
- Will p and q always be present?
'''
class Solution:
    ''' 
    * TC - O(L) where L is the total items in the hashmap | SC - O(max(p, q))
    * 
    * Approach 1: using HASHMAP
    * 1) Put all elements of any one into a hashmap
    * 2) Iterate via other pointer and when you find the current node in map that will be the LCA
    *
    * NOTE: This appoach won't work if there are duplicates in the tree
    '''
    def lowestCommonAncestor(self, p, q):
        map = {}
        current = p
        while current:
            map[current.val] = True
            current = current.parent

        current = q
        while current:
            if current.val in map: return current

            current = current.parent
        
        return False

    ''' 
    * TC - O(D) | SC - O(1) where D is the max of (depth of node 1, depth of node 2)
    * 
    * Approach 1:
    * 1) Find the depth of both p and q
    * 2) Which ever is deepest among the two, bring it up at the same level
    * 3) Now start iterating together and when the two pointers collide that will be LCA
    '''
   
    def getDepth(node):
      depth = 0
      while node:
        node = node.parent
        depth+=1
      return depth
    def lowestCommonAncestor(self, p, q):
      p_depth = self.getDepth(p)
      q_depth = self.getDepth(q)

      for _ in range(p_depth - q_depth):
        p = p.parent
      for _ in range(q_depth - p_depth):
        q = q.parent

		  # Now that they are at the same depth, move them up the tree in parallel until they meet
      while p != q:
        p = p.parent
        q = q.parent
      return p
    
    
    

    def lowestCommonAncestor2(self, p, q):
        def getDepth(root):
            depth = 0

            while root.parent != None:
                depth += 1
                root = root.parent
            return depth
        
        def backTrackTree(lowerDescendant, higherDescendant, depthDiff):
            while depthDiff > 0:
                lowerDescendant = lowerDescendant.parent
                depthDiff -= 1

            while lowerDescendant != higherDescendant:
                lowerDescendant = lowerDescendant.parent
                higherDescendant = higherDescendant.parent

            return lowerDescendant
        
        depthP = getDepth(p)
        depthQ = getDepth(q)

        if depthP > depthQ:
            return backTrackTree(p, q, depthP - depthQ)
        else:
            return backTrackTree(q, p, depthQ - depthP)
    
    ''' 
    * TC - O(H) | SC - O(1)
    * 
    * Approach 3: Linkedlist intersection apprach
    * 1) Keep moving p and q up the ancestor chain untill they meet
    * 2) When one either of the pointer is becoming Null then exchange the pointers
    * 3) This works as after one iteration the pointer deeper than the other will come at the same level as the other one
    * i.e. the deeper pointer would have covered the distance which is difference in depth of the 2
    '''
    def lowestCommonAncestor3(self, p, q):
        p_ptr = p
        q_ptr = q

        while p_ptr != q_ptr:
            p_ptr = p_ptr.parent if p_ptr.parent else q
            q_ptr = q_ptr.parent if q_ptr.parent else p
        
        return p_ptr






"""
# Definition for a Node.
class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        self.parent = None
"""

class Solution:
  def lowestCommonAncestor(self, p, q):
    path = set()
    while p:
      path.add(p)
      p = p.parent
    while q not in path:
      q = q.parent
    return q
    # p1,p2 = p,q
    # while p1 != p2:
    #   p1 = p1.parent if p1 else q
    #   p2 = p2.parent if p2 else p
    
    # return p1
      
      
        
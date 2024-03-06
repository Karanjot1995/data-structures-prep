

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
  def kthSmallest(self, root, k):
    st = []
    curr = root
    n=0

    while True:
      if curr:
        st.append(curr)
        curr = curr.left
      else:
        if not st: break
        node = st.pop()
        n+=1
        if n == k: 
          return node.val
        curr = node.right
      
  # def kthSmallest(self, root, k):
  #   order = []
  #   def traverse(root):
  #     if not root: return
  #     traverse(root.left)
  #     order.append(root.val)
  #     traverse(root.right)
  #   traverse(root)
  #   return order[k-1]

  # def __init__(self):
  #   self.res = 0
  #   self.cnt=0
        
  # def kthSmallest(self, root, k):
  #   def traverse(root):
  #     if not root: return
  #     traverse(root.left)
  #     self.cnt+=1
  #     if self.cnt==k: 
  #       self.res = root.val
  #       return
  #     traverse(root.right)
  #   traverse(root)
  #   return self.res
# Time: O(N)
#Space: O(N)

# Definition for a binary tree node.
class TreeNode:
  def __init__(self, val=0, left=None, right=None):
    self.val = val
    self.left = left
    self.right = right

class Tree:
  def buildTree(self, preorder, inorder) :
    inMap = {inorder[i]:i for i in range(len(inorder)) }
    root = self.traverse(preorder, 0, len(preorder)-1, inorder, 0, len(inorder)-1, inMap)
    print(self.bfs(root))
    return root

  
  def traverse(self, preorder, preStart, preEnd, inorder, inStart, inEnd, inMap):
    if preStart>preEnd or inStart>inEnd: return None

    root = TreeNode(preorder[preStart])
    inRootIdx = inMap[root.val]
    numsLeft = inRootIdx - inStart
    
    root.left = self.traverse(preorder, preStart+1, preStart+numsLeft, inorder, inStart, inRootIdx-1, inMap)
    root.right = self.traverse(preorder, preStart+numsLeft+1, preEnd, inorder, inRootIdx+1, inEnd, inMap)

    return root
  

  #################         Post Order and In Order        ####################

  def buildTreePostIn(self, postorder, inorder):
    inMap = {inorder[i]:i for i in range(len(inorder)) }
    root = self.traverse2( postorder, 0, len(postorder)-1, inorder, 0, len(inorder)-1, inMap)
    print(self.bfs(root))
    return root

  def traverse2(self, postorder, postStart, postEnd, inorder, inStart, inEnd,inMap):
    if postStart>postEnd or inStart>inEnd: return None

    root = TreeNode(postorder[postEnd])
    inRootIdx = inMap[root.val]
    numsLeft = inRootIdx - inStart

    root.left = self.traverse2(postorder, postStart, postStart+numsLeft-1, inorder, inStart, inRootIdx-1, inMap)
    root.right = self.traverse2(postorder,postStart+numsLeft, postEnd-1, inorder, inRootIdx+1, inEnd, inMap)
    return root
  

  def bfs(self, root):
    q = [root]
    res = []
    while q:
      popped = q.pop(0)
      res.append(popped.val)
      if popped.left:
        q.append(popped.left)
      if popped.right:
        q.append(popped.right)
    return res


tree = Tree()

#             10
#           /    \
#         20       30
#       /   \     /  
#      40    50  60

print(tree.buildTree([10,20,40,50,30,60],[40,20,50,10,60,30]))
print(tree.buildTreePostIn([40,50,20,60,30,10],[40,20,50,10,60,30]))
        
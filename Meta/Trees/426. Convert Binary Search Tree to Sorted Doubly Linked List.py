# https://leetcode.com/problems/convert-binary-search-tree-to-sorted-doubly-linked-list/

class Solution:
    '''
    APPROACH 1- Brute Force (Inorder traversal)
    - Inorder traversal for a BST will give the nodes in sorted order
    - Create a list of inorder traversal of the BST and then create connections

    TC - O(N) | SC - O(N)
    '''
    def treeToDoublyList1(self, root):
        if not root:
            return None

        inorder_vals = []

        def inorder(root):
            if not root:
                return
            
            inorder(root.left)
            inorder_vals.append(root)
            inorder(root.right)
        
        inorder(root)
        
        dummy = Node(-1, None, inorder_vals[0])
        prev = dummy
        for i in range(len(inorder_vals) - 1):
            inorder_vals[i].right = inorder_vals[i + 1]
            inorder_vals[i].left = prev
            prev = inorder_vals[i]
        
        prev.right = inorder_vals[-1]
        inorder_vals[-1].left = prev
        prev = inorder_vals[-1]
        prev.right = dummy.right
        dummy.right.left = prev
            
        return dummy.right

    '''
    APPROACH 2 - INPLACE Inorder traversal 
    - When we traverse the tree in inorder traversal we wil take the sorted path
    - So, while we are doing the traversal we can form links between nodes

    TC - O(N)
    SC - O(N) for recursion stack (which will be height of tree which will be logN if the tree is balanced else N if the tree is skewed)
    '''
    def treeToDoublyList(self, root):
        if not root: return None

        head = None
        tail = None

        def inorder(root):
            if not root: return
            nonlocal head, tail            
            inorder(root.left)
            if not head: head = root
            else:
                root.left = tail
                tail.right = root
            tail = root
            inorder(root.right)
        
        inorder(root)
        head.left = tail
        tail.right = head

        return head
    
'''
MORRIS TRAVERSAL: CONSTANT SPACE (not expected in interview)
'''
class Node:
    def __init__(self, val=None, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def treeToDoublyList(root):
    if root:
        head = Node()  # fake node for a start
        prev = head     # remember previous node
        curr = root     # start from the root
        while curr:
            # this is the most left unprocessed node
            if not curr.left:
                curr.left = prev
                prev.right = curr
                prev = curr
                curr = curr.right
            else:
                rightmost = curr.left  # find the rightmost child
                while rightmost.right:
                    rightmost = rightmost.right
                if not rightmost.right:  # found the rightmost
                    rightmost.right = curr
                    temp = curr  # remember curr to invalidate its left pointer
                    curr = curr.left
                    temp.left = None  # we can also set it right away temp.left = rightmost but then we need to check for it
        prev.right = head.right  # at the end prev points to the last node
        head.right.left = prev   # replace fake node with the last node in the tree
        head = head.right
        return head
    return None







"""
# Definition for a Node.
class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
"""

class Solution:
  def treeToDoublyList(self, root):
    if not root: return None

    first, last = None, None

    def dfs(curr):
      nonlocal first, last
      if curr:
        dfs(curr.left)
        if last:
          last.right = curr
          curr.left = last
        else: first = curr
        last = curr
        dfs(curr.right)

    dfs(root)

    last.right = first
    first.left = last

    return first
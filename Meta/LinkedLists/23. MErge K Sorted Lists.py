import heapq
from queue import PriorityQueue

'''
APPROACH 1: Brute Force
Put all the elements in a list, sort them and merge
TC - O(NlogN)
SC - O(N)
'''

'''
APPROACH 2: Merge lists one by one
Take first list and merge with 2nd, take the merged list and merge it with 3rd and so on (convert merge k lists problem to merge 2 lists (k-1) times)

TC - O(kN) where k is the number of linked lists
SC - O(1)
'''

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
  def mergeLists(self, l1,l2):
    head = ListNode(-1)
    tail = head
    while l1 and l2:
      if l1.val<=l2.val:
        tail.next = l1
        l1 = l1.next
      else:
        tail.next = l2
        l2 = l2.next
      tail = tail.next
    
    tail.next = l1 if l1 else l2

    return head.next


  def mergeKLists(self, lists):
    if not lists or len(lists) == 0: return None
    if len(lists)==1: return lists[0]
    st = [lists]
    i = len(lists)-1
    while len(lists)>1:
      l = self.mergeLists(lists[-2], lists[-1])
      lists.pop()
      lists.pop()
      lists.append(l)
      
    return lists[0]
  

  '''
    APPROACH 3: Using Heap
    https://leetcode.com/problems/merge-k-sorted-lists/solutions/1032723/python-heap-solution-explained/
    TC - O(NlogK)
    SC - O(N)
  '''
  def mergeKListsHeap(self, lists):
      dummy = curr = ListNode(0)
      heap = []
      for idx, l in enumerate(lists):
        if l: heapq.heappush(heap, (l.val, idx))
              
      while heap:
        val, idx = heapq.heappop(heap)
        curr.next = ListNode(val)
        curr = curr.next
        node = lists[idx]
        if node.next:
          lists[idx] = node.next
          heapq.heappush(heap, (lists[idx].val, idx))
              
      return dummy.next
  
  '''
    APPROACH 4: Divide and conquer (OPTIMAL)
    This approach walks alongside the one above but is improved a lot. We don't need to traverse most nodes many times repeatedly

    - Pair up k lists and merge each pair.
    - After the first pairing, k lists are merged into k/2 lists with average 2N/k length, then k/4, k/8 and so on.
    - Repeat this procedure until we get the final sorted linked list.

    TC
        - O(Nlogk) where k is the number of linked lists
        - We can merge two sorted linked list in O(n)O(n)O(n) time where nnn is the total number of nodes in two lists
        
    SC - O(1)
  '''
  def mergeKLists(self, lists):
    if not lists or len(lists) == 0: return None

    while len(lists)>1:
      merged = []
      for i in range(0,len(lists),2):
        l1 = lists[i]
        l2 = lists[i+1] if i+1<len(lists) else None
        merged.append(self.mergeLists(l1,l2))
      lists = merged
    return lists[0]





      
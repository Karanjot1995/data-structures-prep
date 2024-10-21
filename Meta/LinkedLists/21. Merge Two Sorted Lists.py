'''
Time complexity : O(n+m)

Because exactly one of l1 and l2 is incremented on each loop
iteration, the while loop runs for a number of iterations equal to the
sum of the lengths of the two lists. All other work is constant, so the
overall complexity is linear.

Space complexity : O(1)

The iterative approach only allocates a few pointers, so it has a
constant overall memory footprint.
'''

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def mergeTwoLists(self, l1, l2):
      head = ListNode()
      tail = head
      while l1 and l2:
        if l1.val <= l2.val:
          tail.next = l1
          l1 = l1.next
        else:
          tail.next = l2
          l2 = l2.next
        tail = tail.next
      
      if l1: tail.next = l1
      if l2: tail.next = l2
      return head.next

      
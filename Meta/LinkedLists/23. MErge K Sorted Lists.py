# https://leetcode.com/problems/merge-k-sorted-lists/description/


import heapq

class Solution:
    def mergeTwoLists(self, l1, l2):
        dummy = ListNode(0)
        tail = dummy
        while l1 and l2:
            if l1.val <= l2.val:
                tail.next = l1
                l1 = l1.next
            else:
                tail.next = l2
                l2 = l2.next
            tail = tail.next

        if l1:
            tail.next = l1

        if l2:
            tail.next = l2

        return dummy.next

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
    def mergeKLists1(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if not lists or len(lists) == 0: return None

        while len(lists) > 1:
            lists.append(self.mergeTwoLists(lists[0], lists[1]))
            lists.pop(0)
            lists.pop(0)
        return lists[0]

    '''
    APPROACH 3: Using Heap
    https://leetcode.com/problems/merge-k-sorted-lists/solutions/1032723/python-heap-solution-explained/
    TC - O(NlogK)
    SC - O(N)
    '''
    def mergeKLists(self, lists):
        dummy = curr = ListNode(0)
        heap = []
        for ind, element in enumerate(lists):
            if element:
                heapq.heappush(heap, (element.val, ind))
                
        while heap:
            val, idx = heapq.heappop(heap)
            curr.next = ListNode(val)
            curr = curr.next
            if lists[idx].next:
                lists[idx] = lists[idx].next
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
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if not lists or len(lists) == 0: return None

        while len(lists) > 1:
            mergedLists = []
            for i in range(0, len(lists), 2):
                l1 = lists[i]
                l2 = lists[i + 1] if (i + 1) < len(lists) else None
                mergedLists.append(self.mergeTwoLists(l1, l2))
            lists = mergedLists
        return lists[0]
    
    '''
    APPROACH 5: QuickSelect
    - If there are "m" arrays and total "N" elements then we can put all the elements in 1 array and do quickselect

    TC - O(N) average (worst case - O(N^2))
    SC - O(N)
    '''

    '''
    APPROACH 6: Median of Medians
    - Improve the Quckselect approach so that the worst case will also be O(N)

    TC - O(N)
    SC - O(N)
    '''
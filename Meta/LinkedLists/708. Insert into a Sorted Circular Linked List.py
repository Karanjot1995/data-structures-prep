# https://leetcode.com/problems/insert-into-a-sorted-circular-linked-list/

class Solution:

    '''
    APPROACH: HANDLE ALL THE EDGE CASES
    - Loop over the LL and add the node, there can be the following 4 cases
        1) IF head is None (empty list)
        2) Normal case insert between nodes prev < newNode < cur
        3) Insert at the end when prev > cur
        4) Uniform values: insert equal value -> insert 10 in 3->3->3->(back to head)

    TC - O(N)
    SC - O(1)
    '''
    def insert(self, head: 'Optional[Node]', insertVal: int) -> 'Node':
        # Case I
        if not head:
            head = Node(insertVal)
            head.next = head
            return head
        
        prev = head
        cur = head.next

        # while we have not done 1 full iteration of the LL since this is a circular LL
        while cur != head:
            # Case II
            if prev.val <= insertVal <= cur.val:
                newNode = Node(insertVal, cur)
                prev.next = newNode

                return head
            elif prev.val > cur.val:
                # Case III: insert at the end
                if insertVal >= prev.val or insertVal <= cur.val:
                    newNode = Node(insertVal, cur)
                    prev.next = newNode

                    return head
            
            prev = cur
            cur = cur.next
        
        # Case IV
        newNode = Node(insertVal, cur)
        prev.next = newNode
        return head
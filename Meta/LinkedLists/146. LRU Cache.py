# https://leetcode.com/problems/lru-cache/description/

class DLinkedListNode:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.prev = None
        self.next = None
'''
APPROACH: Doubly Linked List
- We need a way to store data in an ordered manner such that elements can be removed from any position in constant time so we use DLL
- We make 2 dummy nodes LEFT and RIGHT so it becomes easier for us to add and remove nodes in LL
- The LEFT node will signify the least recently used nodes and the RIGHT node will signify the most recently used nodes
- get()
    - the idea is whenever we get we remove the node form LL and then insert it right before RIGHT
- put()
    - if the node is in cache we remove it and add as a new node right before RIGHT
    - if we grow over the cacpacity then we remove the node right after LEFT

TC
    - get(): O(1)
    - put(): O(1)
SC - O(capacity)
'''
class LRUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        # key -> DLL node
        self.cache = {}
        self.left = DLinkedListNode(0, 0)
        self.right = DLinkedListNode(0, 0)
        
        # left - least recently used
        # right - most recently used
        # elements will be keep on inserting between these two
        self.left.next, self.right.prev = self.right, self.left
        
    def remove(self, node):
        prev, next = node.prev, node.next
        
        prev.next = next
        next.prev = prev
    
    # insert towards right just before self.right (dummy node)
    def insert(self, node):
        prev, next = self.right.prev, self.right
        
        prev.next = node
        next.prev = node
        
        node.next = next
        node.prev = prev

    # TC - O(1)
    def get(self, key: int) -> int:
        if key in self.cache:
            node = self.cache[key]
            
            self.remove(node)
            self.insert(node)
            return node.val
        return -1

    # TC - O(1)
    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            node = self.cache[key]
            self.remove(node)
        self.cache[key] = DLinkedListNode(key, value)
        self.insert(self.cache[key])
        
        if len(self.cache) > self.capacity:
            # remove the least recently used node
            lru = self.left.next
            self.remove(lru)
            del self.cache[lru.key]


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
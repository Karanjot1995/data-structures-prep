# https://leetcode.com/problems/insert-delete-getrandom-o1/description/

'''
ALGORITHM
1) If we see insert and remove in isolation it is pretty easy to implement in constant time using a hash map as addition/removal are constant time
2) But for getRandom() we can simply use an inbuilt python function random.choice() to get a random element from a list in constant time but it cant
   be done by using a hashmap (we cant index a hash map)
3) So what I am thinking is to maintain a hashmap as well as a list so now we can simply use random library to get a random value
4) But now the problem is if we remove a value from end of the array its fine and removing a value fom the hash map is also constant BUT removing a 
   value from the middle of the array is not easy
5) So what I will do is for inserting elements I will always insert at the end of the array
6) For removing element I will use a trick -- so we get the index that is being is removed via the hashmap and to that index we copy the last element
   of the array (and update its position in hashmap) and now we can simply delete the last element in constant time


TC
    - getRandom() is awlays O(1)
    - insert() and delete() is O(1)
SC - O(N)
'''
import random


class RandomizedSet:

    def __init__(self):
        self.nums_map = {}
        self.nums_list = []

    def insert(self, val: int) -> bool:
        if val not in self.nums_map:
            self.nums_map[val] = len(self.nums_list) # index where we will add val
            self.nums_list.append(val)
            return True
        return False

    '''
    Use a trick - when removing val, copy last element at index val, and pop from last
    '''
    def remove(self, val: int) -> bool:
        if val in self.nums_map:
            idx = self.nums_map[val]
            last_val = self.nums_list[-1]

            # move last val at idx and pop from list then delete from hash map
            self.nums_list[idx] = last_val
            self.nums_map[last_val] = idx
            self.nums_list.pop()
            del self.nums_map[val]

            return True
        return False

    def getRandom(self) -> int:
        return random.choice(self.nums_list)


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()
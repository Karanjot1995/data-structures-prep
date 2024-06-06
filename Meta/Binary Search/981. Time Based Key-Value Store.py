'''
Time complexity:

In the set() function, in each call we store a value at (key, timestamp) location, which takes O(L⋅logM) time as the internal implementation of sorted maps is some kind of balanced binary tree and in worst case we might have to compare logM nodes (height of tree) of length L each with our key.
Thus, for MMM calls overall it will take, O(L⋅M⋅logM) time.

In the get() function, we will find correct key in our map, which can take O(L⋅logM)time and then use binary search on that bucket which can have at most M elements, which takes O(logM) time.
peekitem in python will also take O(logN) time to get the value, but the upper bound remains the same.
Thus, for N calls overall it will take, O(N⋅(L⋅logM+logM)) time.

Space complexity:

In the set() function, in each call we store one value string of length L, which takes O(L) space.
Thus, for M calls we may store M unique values, so overall it may take O(M⋅L) space.

In the get() function, we are not using any additional space.
Thus, for all N calls it is a constant space operation.
'''

class TimeMap:

  def __init__(self):
    self.hmap = {}

  
  def set(self, key: str, value: str, timestamp: int) -> None:
    if not key in self.hmap:
      self.hmap[key] = []
    self.hmap[key].append([timestamp, value])
    

  def get(self, key: str, timestamp: int) -> str:
    if not key in self.hmap: return ""
    if timestamp < self.hmap[key][0][0]: return ""

    l = 0
    r = len(self.hmap[key])

    while l<r:
      mid = (l+r)//2
      if self.hmap[key][mid][0]<=timestamp:
        l=mid+1
      else:
        r=mid

    return "" if r==0 else self.hmap[key][r-1][1]
#     for vals in self.hmap[key]:
#       if vals[0]<=timestamp:
#         val = vals[1]
#     return val


'''

Time complexity:

In the set() function, in each call, we store a value at (key, timestamp) location, which takes O(L) time to hash the string.
Thus, for M calls overall it will take, O(M⋅L) time.

In the get() function, in each call, we iterate linearly from timestamp to 1 which takes O(timestamp) time and again to hash the string it takes O(L) time.
Thus, for N calls overall it will take, O(N⋅timestamp⋅L)time.

Note: This approach can be TLE, since the time complexity is not optimal given the current data range in the problem description.

Space complexity:

In the set() function, in each call we store one value string of length L, which takes O(L) space.
Thus, for M calls we may store MMM unique values, so overall it may take O(M⋅L) space.

In the get() function, we are not using any additional space.
Thus, for all N calls it is a constant space operation.
'''

class TimeMap:

  def __init__(self):
    self.hmap = {}

  
  def set(self, key: str, value: str, timestamp: int) -> None:
    if not key in self.hmap:
      self.hmap[key] = {}
    self.hmap[key][timestamp] = value

  def get(self, key: str, timestamp: int) -> str:
    if not key in self.hmap: return ""
    for ts in range(timestamp,0,-1):
      if ts in self.hmap[key]:
        return self.hmap[key][ts]
    return ""




# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)
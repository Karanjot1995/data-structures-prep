import collections

def firstUniqChar(s: str) -> int:
  hmap = collections.Counter(s)
  for i, ch in enumerate(s):
    if hmap[ch]==1: return i
  return -1
  
s = "abcdcd"

print(firstUniqChar(s))
# "abcdcd"
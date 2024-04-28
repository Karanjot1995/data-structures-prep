from queue import deque

class Solution:
  def wordBreak(self, s: str, wordDict) -> bool:
    words = set(wordDict)
    q = deque([0])
    seen = set()

    while q:
      start = q.popleft()
      print(start)
      if start == len(s): return True
      for end in range(start+1, len(s)+1):
        if end in seen: continue
        if s[start:end] in words:
          print(start, end, s[start:end])
          q.append(end)
          seen.add(end)
    return False
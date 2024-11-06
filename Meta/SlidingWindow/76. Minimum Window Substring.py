class Solution:
  def minWindow(self, s: str, t: str) -> str:
    hmap = collections.Counter(t)

    char_counter = {}
    l,r = 0,0

    formed_length = 0

    res = [float('inf'), None, None]
    while r<len(s):
      ch = s[r]
      char_counter[ch] = char_counter.get(ch,0)+1
      print(ch , char_counter)
      if ch in hmap and char_counter[ch] == hmap[ch]:
        formed_length+=1

      while l<=r and formed_length == len(hmap):
        char = s[l]
        if r-l+1< res[0]: res = [r-l+1, l, r]
        print(res)
        char_counter[char]-=1

        if char in hmap and char_counter[char]< hmap[char]:
          formed_length -= 1
        l+=1
      r+=1

    return "" if res[0]==float('inf') else s[res[1]:res[2]+1]
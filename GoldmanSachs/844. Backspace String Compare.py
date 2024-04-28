class Solution:

  '''
    APPROACH 1: Stack
    TC - O(s + t)
    SC - O(s + t)
  '''
  def backspaceCompare(self, s: str, t: str) -> bool:

    def build(Str):
      a = []
      for ch in Str:
        if ch != '#': a.append(ch)
        elif a: a.pop()
      return "".join(a)

    return build(s)==build(t)
  
  '''
  APPROACH 2: Two pointer
  - Video: https://www.youtube.com/watch?v=k2qrymM_DOo&ab_channel=NeetCodeIO

  TC - O(N)
  SC - O(1)
  '''
  def backspaceCompare(self, s: str, t: str) -> bool:
      def nextValidChar(str, index):
          backspaceCount = 0
          while index >= 0:
              if backspaceCount == 0 and str[index] != "#":
                  break
              elif str[index] == "#":
                  backspaceCount += 1 # can have multiple backspaces together
              else:
                  backspaceCount -= 1 # skip the characters until we have backspaceCount > 0
              index -= 1

          return index
      
      index_s, index_t = len(s) - 1, len(t) - 1
      while index_s >= 0 or index_t >= 0: # if one of the index goes out of bounds we return False in the loop so "or" instead of "and"
          index_s = nextValidChar(s, index_s)
          index_t = nextValidChar(t, index_t)

          char_s = s[index_s] if index_s >= 0 else "" # make sure it is in bounds
          char_t = t[index_t] if index_t >= 0 else ""

          if char_s != char_t:
              return False
          
          index_s -= 1
          index_t -= 1
      return True
  




    

        
class Solution:
  #space optimal O(1)
  def minRemoveToMakeValid(self, s: str) -> str:
    def removeInvalidClosing(strng, open, close):
      st = []
      extra = 0
      for i,c in enumerate(strng):
        if c == open: extra+=1
        if c == close:
          if extra == 0: continue
          extra-=1
        st.append(c)
      return "".join(st)
    s = removeInvalidClosing(s,'(',')')
    s = removeInvalidClosing(s[::-1],')','(')
    return s[::-1]



  #brute force using O(N) space of stack
  def minRemoveToMakeValid(self, s: str) -> str:
    s = list(s)
    st =[]
    for i in range(len(s)):
      if s[i] == '(': st.append(i)
      elif s[i] == ')':
        if not st: s[i]=""
        else: st.pop()
    
    while st:
      s[st.pop()] = ""
    return "".join(s)


  def minRemoveToMakeValid(self, s: str) -> str:
    st = []
    new_str = ''
    to_rmv_idxs = []
    for i, c in enumerate(s):
      if c == '(': 
        st.append(i)
      elif c == ')': 
        if not st: to_rmv_idxs.append(i)
        else: st.pop()

    to_rmv_idxs = set(st+to_rmv_idxs)
    
    for i,c in enumerate(s):
      if i not in to_rmv_idxs:
        new_str+=c
    return new_str
        
'''
Time complexity : O(n) because we simply traverse the given string one character at a time and push and 
pop operations on a stack take O(1) time.

Space complexity : O(n) as we push all opening brackets onto the stack and in the worst case,
we will end up pushing all the brackets onto the stack. e.g. ((((((((((.
'''

class Solution:
  def isValid(self, s: str) -> bool:
    dict = {'{':'}', '[':']', '(':')'}
    st = []
    for ch in s:
      if ch in dict:
        st.append(ch)
      else:
        if st and dict[st[-1]]==ch:
          st.pop()
        else:
          return False
    return len(st)==0
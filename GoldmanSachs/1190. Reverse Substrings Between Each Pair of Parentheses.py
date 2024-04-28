class Solution:
  def reverseParentheses(self, s: str) -> str:
    st = []
    word = ''
    for ch in s:
      if ch == ')':
        while st and st[-1] != "(":
          word += st.pop()
        st.pop()
        for char in word:
          st.append(char)
        word = ""
      else: st.append(ch)

    return "".join(st)
  

# Input: s = "(u(love)i)"
# Output: "iloveu"
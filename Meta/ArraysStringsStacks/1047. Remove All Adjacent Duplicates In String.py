class Solution:
  #Time complexity : O(N), where N is a string length.
  #Space complexity : O(N−D), where D is a total length for all duplicates.
  
  def removeDuplicates(self, s: str) -> str:
    st = []
    for c in s:
      if st and st[-1]==c:
        st.pop()
      else: st.append(c)
    return ''.join(st)
  
    # st = [s[0]]
    # for i in range(1,len(s)):
    #   if not st or s[i]!=st[-1]:
    #     st.append(s[i])
    #   else: st.pop()
    # return ''.join(st)
def smallestNumber(pattern: str) -> str:
  ans = []
  st = []
  for i in range(len(pattern)+1):
    st.append(str(i+1))
    if i == len(pattern) or pattern[i] == 'I':
      while st: ans.append(st.pop())
  return ''.join(ans)
        


# Input: pattern = "IIIDIDDD"
# Output: "123549876"
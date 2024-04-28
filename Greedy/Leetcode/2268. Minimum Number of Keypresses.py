from collections import Counter

def minimumKeypresses(s: str) -> int:
  hmap = Counter(s)
  counter = 0
  cnt = 0
  presses = 1
  for key,val in enumerate(sorted(hmap.values(), reverse=True)):
    cnt += presses * val
    counter+=1

    #if keypad digit reaches the 9th place presses will be incremented by 1
    if counter > 8:
      counter = 0
      presses+=1

  return cnt

s = "apple"
print(minimumKeypresses(s))


# Output: 5
# Explanation: One optimal way to setup your keypad is shown above.
# Type 'a' by pressing button 1 once.
# Type 'p' by pressing button 6 once.
# Type 'p' by pressing button 6 once.
# Type 'l' by pressing button 5 once.
# Type 'e' by pressing button 3 once.
# A total of 5 button presses are needed, so return 5.
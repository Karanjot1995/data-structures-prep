from collections import defaultdict
'''
Take example and check: ["acd", "dfg", "mop"] these will be grouped together, WHY?

EDGE CASES: "yab" -> "a" - "y" < 0 -> should i consider it circular?

KEY INSIGHT
From "acd" to "dfg" if we add 3 to each char of "acd" we get "dfg"

For "acd"
- "a" -> "c" -> 2 steps
- "c" -> "d" -> 1 step
- KEY to hash will be (2, 1)

For "dfg"
- "d" -> "f" -> 2 steps
- "f" -> "g" -> 1 step
- KEY to hash will be (2, 1)

For "mop"
- "m" -> "o" -> 2 steps
- "o" -> "p" -> 1 step
- KEY to hash will be (2, 1)

OBSERVATION
Same shifting sequence == Follows the same internal pattern ([abs(c - a), abs(d - a)] == [abs(f - d), abs(g - f)] == [abs(o - m), abs(p - o)])

ALGORITHM
1) Find the internal pattern of the string and hash it
2) Create a hashmap with keys as pattern and values as the strings
3) Return the values of the hashpmap

TC - O(NK) | SC - O(NK), where N is the len of the input arr and K is the max len of the strings given in the input

SOURCES
WHY WE ADD +26 to diff -> https://youtu.be/uEXJSRLqoKY?si=lzD2l6HQB13WYOTc&t=305
'''
def groupStrings(strings):
  hmap = defaultdict(list)

  for s in strings:
    seq = ''
    for i in range(len(s)-1):
      curr, nxt = ord(s[i]), ord(s[i+1])
      diff = nxt-curr
      # for word "yab" the diff between "a" - "y" will be negative (97 - 121 = -24) and since we are treating it as circular we add 26 to it, so the diff will be 26 - 24 = 2
      if diff<0: diff+=26
      seq+= str(diff)+' '
    hmap[seq].append(s)
  
  return list(hmap.values())

print(groupStrings(["abc","bcd","acef","xyz","az","ba","a","z"]))


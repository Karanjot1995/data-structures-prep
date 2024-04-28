# https://docs.google.com/document/d/1DtDEC4ocQ4z3BpPxe-_R-8UI6JqQeRMNA3WPdBCpGyo/edit#heading=h.irmprcowrzu3

from collections import deque
'''
GENERAL APPROACH
- Put the first segment in a DS (yet to decide) and remove that segment from the input (so we make a copy of input)
- Then check if there exist a segment in the array whose end (tuple[1]) is equal to cur_segment's first (typle[0]) then append that to left of cur_segment
- Also check if there exist a segment in the array whose start (tuple[0]) is equal to cur_segment's second (typle[1]) then append that to right of cur segment
'''


'''
APPROACH 1: Brute Force
- Using two loops, a copy array, an ans deque (that contains sorted segments)

TC - O(N^2)
SC - O(N)
'''
def sortSegmentsBrute(segments):
    if not segments or len(segments) == 0:
        return []
    
    copy = list(segments)
    
    ans = deque([copy.pop(0)])
    
    while copy:
      size = len(copy)
      for i in range(size - 1, -1, -1):
        start, last = ans[0], ans[-1]
        cur_segment = copy[i]
        if start[0] == cur_segment[1]:
          ans.appendleft(cur_segment)
          copy.pop(i)
        elif last[1] == cur_segment[0]:
          ans.append(cur_segment)
          copy.pop(i)
      # if the size of copy is still same so we did not pop anything from array so the input is INVALID
      if len(copy) == size:
        raise ValueError("Invalid input")
    return list(ans)
print(sortSegmentsBrute([(4,5), (9, 4), (5, 1), (11, 9)]))

'''
APPROACH 2: Hashmap
- Using a loop, 2 hashmaps for start of all segments {start: segment} and a map for end of all segments {end: segment}, ans deque (that contains sorted segments)

TC - O(N)
SC - O(N)
'''
def sortSegments(segments):
    if not segments or len(segments) == 0:
        return []
    start_map = { s[0]: s for s in segments }
    end_map = { s[1]: s for s in segments }
    
    start, end = segments[0]
    ans = deque([segments[0]])

    while True:
      next_segment = start_map.get(end)
      if next_segment: ans.append(next_segment)

      prev_segment = end_map.get(start)
      if prev_segment: ans.appendleft(prev_segment)

      start, end = ans[0][0], ans[-1][1]
      if not prev_segment and not next_segment:
        break
    
    if len(ans) != len(segments):
      raise ValueError("Invalid input")
    
    return list(ans)

# Example -> op: [(11, 9), (9, 4), (4, 5), (5, 1)]
print(sortSegments([(4,5), (9, 4), (5, 1), (11, 9)]))

# Empty segments -> op: []
print(sortSegments([]))

# None -> op: []
print(sortSegments(None))

# Missing segments -> op: ValueError
print(sortSegments([(1, 2), (2, 3), (4, 5), (5, 6)]))

# Duplicates -> op: ValueError
print(sortSegments([(1, 2), (2, 3), (1, 2)]))
from collections import defaultdict
from itertools import combinations


# https://leetcode.com/problems/analyze-user-website-visit-pattern/

def mostVisitedPattern(username, timestamp, website):
  web_info = []

  for time, user, web in zip(timestamp, username, website):
    web_info.append((time, user, web))
  web_info.sort()

  hmap = defaultdict(list) 
  for time, user, web in web_info:
    hmap[user].append(web)

  possibleRoutes = defaultdict(int)
  for usr in hmap:
      routes = set(combinations(hmap[usr], 3))
      for route in routes:
          possibleRoutes[route] += 1


  maxVal, routes = max(possibleRoutes.values()), []
  for r, val in possibleRoutes.items():
    if val == maxVal:
      routes.append(r)
  
  if len(routes)>1:
    routes.sort()
    
  return routes[0]


username = ["joe","joe","joe","james","james","james","james","mary","mary","mary"]
timestamp = [1,2,3,4,5,6,7,8,9,10]
website = ["home","about","career","home","cart","maps","home","home","about","career"]

print(mostVisitedPattern(username, timestamp, website))

  # for i in range(1,n):
  #   # print(prev_user, pattern)
  #   if prev_user == username[i]:
  #     pattern.append(website[i])
  #   else:
  #     hmap[prev_user]=pattern
  #     prev_user = username[i]
  #     pattern = [website[i]]
  #   if i == n-1:
  #     hmap[prev_user] = pattern

  # pattern_cnt = defaultdict(int)
  # for arr in hmap.values():
  #   pattern = ",".join(arr)
  #   pattern_cnt[pattern]+=1
  # print(pattern_cnt)

  


    


        
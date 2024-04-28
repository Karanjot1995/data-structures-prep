import heapq
from collections import defaultdict
    
def IPfreqCount(addresses):
  maxi = 0
  hmap={}

  for addr in addresses:
    addr = addr.split()[0]
    hmap[addr] = hmap.get(addr, 0)+1
    maxi = max(maxi, hmap[addr])

  maxIp = [ip for ip, count in hmap.items() if count == maxi]

  if len(maxIp) > 1:
    return ','.join(sorted(maxIp))
  else:
    return maxIp[0]


addresses = ["10.0.0.1 - GET 2020-08-24", "10.0.0.1 - GET 2020-08-24", "10.0.0.2 - GET 2020-08-20"]
print(IPfreqCount(addresses))



#T=O(nm+nlgk), S=O(k+n)
#n=number of logs,m=len(log),k=top item count
def topIpLogs(logs, k):
    k = 10
    logs = ["10.0.0.1 - GET 2020-08-24", "10.0.0.1 - GET 2020-08-24", "10.0.0.2 - GET 2020-08-20"]
    d = defaultdict(int)
    
    for log in logs:
        ip = log.split()[0]
        d[ip] += 1
    
    min_heap = []
    for ip,f in d.items():
        heapq.heappush(min_heap,(f,ip))
        if len(min_heap) > k:
            heapq.heappop(min_heap)
    
    res = []
    while min_heap:
        res.append(heapq.heappop(min_heap)[1])
    return res

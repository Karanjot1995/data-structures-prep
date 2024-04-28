from collections import defaultdict

def countNicePairs(nums) -> int:
  hmap = defaultdict(int)
  cnt = 0
  MOD = 10 ** 9 + 7

  for i in range(len(nums)):
    rev_str = str(nums[i])[::-1]
    rev = int(rev_str)
    rem = nums[i]-rev
    if rem in hmap: 
      cnt += hmap[rem]
      hmap[rem] += 1
    else: hmap[rem] = 1

  return cnt%MOD


def countNicePairs2(nums) -> int:
  hmap = defaultdict(int)
  cnt = 0
  MOD = 10 ** 9 + 7

  def revNum(n):
    res = 0
    while n: 
      res = res * 10 + n % 10
      n = n // 10
    return res

  for i in range(len(nums)):
    rev = revNum(nums[i])
    rem = nums[i]-rev
    if rem in hmap: 
      cnt += hmap[rem]
      hmap[rem] += 1
    else: hmap[rem] = 1

  return cnt%MOD



        
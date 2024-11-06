def rodCutting(n, price):
  #rem is the total rod length

  def rec(i,rem):
    if i == n-1: 
      if i+1 == rem: return rem//(i+1) * price[i]
      return 0
         
    take = float("-inf")
    rod_length = i+1
    if rod_length<=rem:
      take = price[i] + rec(i, rem-rod_length)

    not_take = 0+rec(i+1,rem)
    return max(take, not_take)

  return rec(0,n)

n = 8
price = [1, 5, 8, 9, 10, 17, 17, 20]
print(rodCutting(n, price))

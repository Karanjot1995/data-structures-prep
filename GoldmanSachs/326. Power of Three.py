def isPowerOfThree(n: int) -> bool:
  if n < 1: return False
  while n % 3 == 0:
      n = n//3
  return n == 1

  # if n <= 0: return False
  # logValue = log10(n) / log10(3)
  # return logValue == int(logValue)
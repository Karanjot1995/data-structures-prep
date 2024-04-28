def smallestDivisor(n):
 
    # if divisible by 2
    if (n % 2 == 0):
        return 2
 
    # iterate from 3 to sqrt(n)
    i = 3; 
    while(i * i <= n):
        print(i,i*i)
        if (n % i == 0):
            return i
        i += 2
 
    return n
 
 
# Driver Code
n = 315
print(smallestDivisor(n))


def primeFactors(n):
  res = ''
  while n % 2 == 0:
    res+='2' + " "
    n /= 2

  # n must be odd at this point.  So we can
  # skip one element (Note i = i +2)
  i = 3; 
  while(i * i <= n):
    while n % i == 0:
      res+=str(i) + " "
      n /= i
    i+=2

    # This condition is to handle the case when
    # n is a prime number greater than 2
  if (n > 2): res+=str(int(n))
  return res

print(primeFactors(n))
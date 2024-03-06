def rec(i,n):
  if i > n : return
  print('Karan')
  rec(i+1,n)
print(rec(1,5))


def NtoOne(i,n):
  if i<n: return
  print(i)
  NtoOne(i-1,n)
print(NtoOne(5,1))




#TC -> O(N)
#SC -> O(N)

# backtracking -> last guy executed first
def oneToN(i,n):
  if i < 1: return
  oneToN(i-1,n)
  print(i)
print(oneToN(5,5))


#Sum on first N using parametrized
def sum_n(i,sum):
  if i<1:
    print(sum)
    return
  sum_n(i-1,sum+i)
sum_n(5,0)

#Sum on first N using functional
def sumN(n):
  if n ==0: return 0
  return n + sumN(n-1)

print(sumN(5))


#Factorial on first N using parametrized
def factN(i,prod):
  if i==1:
    print('fact parameterized: ',prod)
    return
  factN(i-1,prod*i)
factN(5,1)

#Factorial on first N using functional
def fact(n):
  if n == 1: return 1
  return n*fact(n-1)

print(fact(5))



# Reverse Array

def revArr(arr):
  def rev(i,j):
    if i>=j: return
    arr[i], arr[j] = arr[j], arr[i]
    rev(i+1,j-1)
  rev(0,len(arr)-1)
  return arr

arr = [1,2,3,4,5]
print(revArr(arr))

# when the problem statement will say count all ways, count/try all possible ways, count distinct ways,
# what gives you the minimum or max output then we apply recursion
# shortcut
# try to represent the problem in terms of an index
# do all possible stuffs on that index according to the problem statement
# if the question says count all ways -> sum up all the stuffs
# eg ->  ques says find min/max => take min/max of all stuffs


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



# Reverse Array using pointers
def revArr(arr):
  def rev(i,j):
    if i>=j: return
    arr[i], arr[j] = arr[j], arr[i]
    rev(i+1,j-1)
  rev(0,len(arr)-1)
  return arr

arr = [1,2,3,4,5]
print('rev: ', revArr(arr))


# Reverse Array without using pointers

def revArrOnePointer(arr):
  n = len(arr)
  def rev(i):
    if i>=n/2: return
    arr[i], arr[n-i-1] = arr[n-i-1], arr[i]
    rev(i+1)
  rev(0)
  return arr

arr = [1,2,3,4,5]
print('rev one pointer: ', revArrOnePointer(arr))



def isPalindrome(s):
  # def rec(i,j):
  #   if i>=j: return True
  #   if s[i]!=s[j]: return False
  #   return rec(i+1,j-1)
  # return rec(0,len(s)-1)
  n = len(s)
  def rec(i):
    if i>=n/2: return True
    if s[i]!=s[n-i-1]: return False
    return rec(i+1)
  return rec(0)

print(isPalindrome("acacbcaca"))


# TC -> O(2^n) : exponential
def fibonacci(n):
  if n <=1: return n
  return fibonacci(n-1)+fibonacci(n-2)

print(fibonacci(7))




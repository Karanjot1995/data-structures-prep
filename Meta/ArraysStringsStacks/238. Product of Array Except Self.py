class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prod = 1
        zeroes = 0
        for num in nums:
            if num!=0:
                prod *= num
            else:
                zeroes+=1
        if zeroes>1: return [0]*len(nums)
        arr = []
        for num in nums:
            if not zeroes:
                arr.append(int(prod/num))
            elif zeroes == 1 and num==0:
                arr.append(int(prod))
            else:
                arr.append(0)
        return arr
        

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        length = len(nums)
        L, R, answer = [0] * length, [0] * length, [0] * length

        L[0] = 1
        for i in range(1, length):
            L[i] = nums[i - 1] * L[i - 1]
        R[length - 1] = 1
        for i in reversed(range(length - 1)):
            R[i] = nums[i + 1] * R[i + 1]
        for i in range(length):
            answer[i] = L[i] * R[i]

        return answer
    

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        length = len(nums)
        answer = [0] * length
        answer[0] = 1
        
        for i in range(1, length):
            answer[i] = nums[i - 1] * answer[i - 1]
        R = 1

        for i in reversed(range(length)):
            answer[i] = answer[i] * R
            R *= nums[i]

        return answer
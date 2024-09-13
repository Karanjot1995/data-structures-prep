# https://leetcode.com/problems/minimum-add-to-make-parentheses-valid/description/

'''
CLARIFTING QUESTIONS

- empty string?
- null string
- will string only contain parantheses or other characters
'''

class Solution:
    '''
    APPROACH 1: STACK
    - Simlar to checking if the string is valid parantheses or not (LC 20)
    - We will keep track of invalid parentheses in a stack
    - Length of stack will be the min parantheses needed to be added
    
    TC - O(N)
    SC - O(N)
    '''
    def minAddToMakeValid1(self, s: str) -> int:
        stack = []

        for char in s:
            if char == "(":
                stack.append(char)
            else:
                # char is ")"
                if stack and stack[-1] == "(":
                    stack.pop()
                else:
                    stack.append(char)
        
        return len(stack)
    
    '''
    APPROACH 2: NO STACK
    - instead of using stack we can use 2 variables to keep track of opening and closing
    - we just balance the parantheses as we see opening and closing
    - in the end we would return addition of opening and closing
    
    TC - O(N)
    SC - O(1)
    '''
    def minAddToMakeValid(self, s: str) -> int:
        opening = closing = 0

        for char in s:
            if char == "(":
                opening += 1
            else:
                if opening: opening -= 1
                else:
                    closing += 1
        
        return opening + closing




# class Device(object) :
#     def __init__(self, device_id):
#         self._device_id = device_id
#         self._latest_data = 12

#     @property
#     def latest_data(self) :
#         return self._latest_data
    
#     @latest_data.setter
#     def latest_data(self, val):
#         self._latest_data = val

#     def get_data(self):
#         return self.latest_data
    
# class EnvironmentalChamber(Device):
#     def __init__(self, device_id):
#         self._latest_data = 3
#         super(EnvironmentalChamber, self).__init__(device_id)
    
# class PowerSupply(Device):
#     def __init__(self, device_id):
#         super(PowerSupply, self).__init__(device_id)
#         self._latest_data = 25

#     def get_data(self) :
#         return self.latest_data * 2
    
# class TestComponent(Device) :
#     def get_data(self) :
#         return self._latest_data + 8
    
# def my_func():
#     chamber = EnvironmentalChamber("1234")
#     # print(chamber.get_data())
#     psu = PowerSupply("5678")
#     component = TestComponent("9012")
#     print(chamber.latest_data, psu.latest_data, component.latest_data)
#     return chamber.get_data() + psu.get_data() + component.get_data()

# print(my_func())


# def my_func (num_list) :
# 	output = []
# 	for index in range(0, len(num_list)):
#         current_num = num_list[index]
#         if len(output)<3:
#             output.insert(0, current_num) # insert current_num to the beginning of 
#         elif current_num > output [0]:
#             output [0] = current_num
#         if len(output)>1:
#             for k in range(1, len(output)):
#                 if output[k]<output[k-1]:
#                     temp_val = output[k]
#                     output[k] = output[k - 1]
#                     output [k - 1] = temp_val
# 	return output
        

# def my_func(num_list):
#     output = []
#     for index in range(len(num_list)):
#         current_num = num_list[index]
#         print(current_num)
#         if len(output) < 3:
#             output.insert(0, current_num)  # Insert current_num at the beginning of the list
#         elif current_num > output[0]:
#             output[0] = current_num  # Replace the smallest element if current_num is larger
        
#         # Sort the list to ensure it is in non-decreasing order
#         print(output)

#         if len(output) > 1:
#             for k in range(1, len(output)):
#                 if output[k] < output[k - 1]:
#                     output[k], output[k - 1] = output[k - 1], output[k]
#         print('swapped', output)
                    
#     return output


# print(my_func([5, 1, 4, 100, 1000, 7, 3, 6, 100000, -1]))





# def my_func(num_list):
#     if len(num_list) < 3:
#         return 0, None  # Not enough numbers to form any 3-number average
    
#     count = 0
#     peak_avg = float('-inf')
#     peak_dataset = None

#     for i in range(3, len(num_list)):
#         # Calculate the average of the last 3 numbers
#         avg_last_3 = sum(num_list[i-3:i]) / 3
        
#         # Check if the next number is larger than the average
#         if num_list[i] > avg_last_3:
#             count += 1
        
#         # Identify the peak average dataset
#         if avg_last_3 > peak_avg:
#             peak_avg = avg_last_3
#             peak_dataset = num_list[i-3:i]
    
#     return count, peak_dataset

# # Example usage
# # num_list = [5, 8, 12, 15, 7, 10, 20, 25]
# num_list = [5,2,2,8,1,7,11,0]
# count, peak_dataset = my_func(num_list)
# print("Count of numbers larger than the average of the last 3:", count)
# print("Peak average dataset:", peak_dataset)
    

from collections import defaultdict


def solution(words):
    slice_count = {}
    count = 0

    for i,word in enumerate(words):
        if word in slice_count:
            count+=slice_count[word]

        for j in range(1,len(word)):
            sliced_word = word[j:]
            print(sliced_word, words[:i] + words[i + 1:], slice_count)
            if sliced_word in (words[:i] + words[i + 1:]):
                count += slice_count.get(sliced_word, 1)
        slice_count[sliced_word] = slice_count.get(sliced_word, 0) + 1
        
    print(slice_count, count)


        


    # for word in words:
    #     length = len(word)

    #     # Check if this word is already the suffix of some previous words
    #     if word in slice_count:
    #         count += slice_count[word]

    #     # Generate slices that include the end of the string
    #     for i in range(1, length):
    #         slice = word[i:]

    #         # Count the occurrences of each slice
    #         if slice in slice_count:
    #             count += slice_count[slice]

    #         # Update slice_count
    #     slice_count[slice] = slice_count.get(slice, 0) + 1

    return count


# def solution(words):
    
#     suffix_map = defaultdict(int)
#     word_map = defaultdict(int)
#     count = 0

#     for word in words:
#         word_map[word] += 1
#         for i in range(len(word) - 1, 0, -1):
#             suffix = word[i:]
#             suffix_map[suffix] += 1

#     for word, _ in word_map.items():
#         if word_map[word] > 1 and suffix_map[word] < 1:
#             count += word_map[word] * (word_map[word] - 1) / 2
#         elif word_map[word] >= 1 and suffix_map[word] >= 1:
#             count += word_map[word] * (word_map[word] - 1) / 2
#             count += word_map[word] * suffix_map[word]
#     return count

# def solution(strings):
#     sorted = [s[::-1] for s in strings]
#     sorted.sort()

#     matchCounts = []
#     prevstr = ''
#     count = 0
#     for s in sorted:
#         for i in range(min(len(prevstr), len(s))):
#             if s[i] != prevstr[i]:
#                 del matchCounts[i:]
#                 break
#             count+=matchCounts[i]
#         while len(matchCounts) < len(s):
#             matchCounts.append(0)
#         matchCounts[len(s)-1] += 1
#         prevstr = s
#     return count

# words = ["back", "backdoor", "gammon", "backgammon", "comeback", "come", "door"]
words = ["cba", "a", "a", "b", "ba"]
print(solution(words))
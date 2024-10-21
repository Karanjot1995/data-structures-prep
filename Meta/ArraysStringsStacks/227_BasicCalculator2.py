class Solution:
	''' 
	APPROACH 2 OPTIMAL without stack (CONVERTING above approach to this)
	For simple "2+3+4" we can simple keep a total to evaluate the operation
	But for "2+3*2" we can't just add 2 + 3 as it would result in wrong answer (2 + 3 = 5 then 5*2 = 10 i.e. wrong)
	We must evaluate the (+) and (-) expression later based on the next operation
	
	TC - O(N)
	SC - O(1)
	'''
	def calculate(self, s):
		if not s or len(s) == 0: return 0

		cur = 0
		cur_operation = "+"
		prev = total = 0

		for i in range(len(s)):
				if s[i].isdigit():
						cur = (cur * 10) + int(s[i])

				# i == len(s) - 1 to push the last number which will not be an operator
				if s[i] in "+-*/" or i == len(s) - 1:
						if cur_operation == "+":
								total += cur

								prev = cur
						elif cur_operation == "-":
								total -= cur

								prev = -cur
						elif cur_operation == "*":
								total -= prev # undo the last operation
								total += prev * cur

								prev = cur * prev
						else:
								total -= prev
								total += int(prev / cur) # as prev // cur does not work properly if the num is negative

								prev = int(prev / cur)
						
						cur_operation = s[i]
						cur = 0
		
		return total
	
	# TC - O(N)
	# SC - O(N)
  # def calculate2(self, s: str) -> int:    
  #   st = []
  #   cur_num = 0
  #   operation = "+"
  #   for i,c in enumerate(s):
  #     if c.isdigit():
  #       cur_num = cur_num*10 + int(c)
      
  #     if c in "+-*/" or i == len(s)-1:
  #       if operation == "+": st.append(cur_num)
  #       elif operation == "-": st.append(-cur_num)
  #       elif operation == "*":
  #         prev_num = st.pop()
  #         st.append(int(prev_num*cur_num))
  #       elif operation == "/":
  #         prev_num = st.pop()
  #         st.append(int(prev_num/cur_num))

  #       operation = c
  #       cur_num = 0

  #   ans = 0
  #   for num in st: ans+= num
  #   return ans
        

  # def calculate3(self, s: str) -> int:    
  #   st = []
  #   cur_num = 0
  #   operation = "+"
  #   i = 0
  #   while i<len(s):
  #     if s[i].isdigit():
  #       cur_num = int(s[i])
  #       while i+1<len(s) and s[i+1].isdigit():
  #         cur_num = cur_num*10 + int(s[i+1])
  #         i+=1
  #       if operation == "+": st.append(cur_num)
  #       elif operation == "-": st.append(-cur_num)
  #       if operation == "*": 
  #         prev_num = st.pop()
  #         st.append(int(prev_num*cur_num))
  #       if operation == "/": 
  #         prev_num = st.pop()
  #         st.append(int(prev_num/cur_num))
  #     else:
  #       if s[i] != ' ': operation = s[i]
  #     i+=1

  #   ans = 0
  #   for num in st: ans+= num
  #   return ans

s = "3+2*2"

        
        

class Solution:
  def calculate(self, s: str) -> int:
    def evaluate(x, y, operator):
      if operator == "+":
        return x
      if operator == "-":
        return -x
      if operator == "*":
        return x * y
      return int(x / y)

    st = []
    curr_num = 0
    operation = '+'
    i=0
    s += " "

    for c in s:
      # if c == " ": continue
      if c.isdigit():
        curr_num = curr_num*10+int(c)
      elif c == "(":
        st.append(operation)
        operation = "+"
      else:
        if operation in "*/":
          st.append(evaluate(st.pop(), curr_num, operation))
        else:
          st.append(evaluate(curr_num, 0, operation))
        
        curr_num = 0
        operation = c
        print(operation)
        if c == ")":
          while type(st[-1]) == int:
            curr_num += st.pop()
          operation = st.pop()

    return sum(st)





    # while i<len(s):
    #   if 
    #   if s[i] == '(':
    #     st.append(s[i])
    #     operation = "+"
    #   elif s[i].isdigit():
    #     currNum = int(s[i])
    #     while i+1<len(s) and s[i+1].isdigit():
    #       currNum = currNum*10+int(s[i+1])
    #       i+=1
    #     if operation == '+': st.append(currNum)
    #     elif operation == '-': st.append(-currNum)
    #     elif operation == '*': 
    #       prevNum = st.pop()
    #       print('multiply: ', prevNum, currNum)
    #       st.append(int(prevNum*currNum))
    #     elif operation == '/': 
    #       prevNum = st.pop()
    #       print('divide: ', prevNum, currNum)
    #       st.append(int(prevNum/currNum))
    #   elif s[i] == ')':
        
    #   else:
    #     if s[i]!=' ': operation = s[i]
    #   i+=1

    # res = 0
    # for d in st:
    #   res+=d
    # return res
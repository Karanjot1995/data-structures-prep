def calculate(s):
	st = []
	currNum = 0
	operation = '+'
	i=0
	while i<len(s):
		if s[i].isdigit():
			currNum = int(s[i])
			while i+1<len(s) and s[i+1].isdigit():
				currNum = currNum*10+int(s[i+1])
				i+=1
			if operation == '+': st.append(currNum)
			elif operation == '-': st.append(-currNum)
			elif operation == '*': 
				prevNum = st.pop()
				print('multiply: ', prevNum, currNum)
				st.append(int(prevNum*currNum))
			elif operation == '/': 
				prevNum = st.pop()
				print('divide: ', prevNum, currNum)
				st.append(int(prevNum/currNum))
		else:
			if s[i]!=' ': operation = s[i]
		i+=1

	res = 0
	for d in st:
		res+=d
	return res

s = "3+2*2"
print(calculate(s))

        
        

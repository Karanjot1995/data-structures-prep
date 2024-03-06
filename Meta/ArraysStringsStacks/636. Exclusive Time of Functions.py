# APPROACH 1: Penalty based (USE THIS)

# TC - O(N)
# SC - O(N)

def exclusiveTime(n: int, logs):
  ans = [0]*n
  st = []
  for log in logs:
    process_id, event, time = log.split(":")
    process_id = int(process_id)
    time = int(time)
    if event == 'start':
      st.append([process_id,time])
    elif event == 'end':
      process_id, start_time = st.pop()
      #time spent for current process
      time_spent = time - start_time+1
      ans[process_id] += time_spent
      if st:
        #remove the current process time spent from any previous processes running
        prev_process_id, t = st[-1]
        ans[prev_process_id] -= time_spent
  
  return ans


n = 2
logs = ["0:start:0","1:start:2","1:end:5","0:end:6"]
print(exclusiveTime(n,logs))
#Output: [3,4]





#other approach
def exclusiveTime(self, n: int, logs):
  execution_times = [0] * n
  call_stack = []
  prev_start_time = 0

  for log in logs:
      func_id, call_type, timestamp = log.split(":")
      func_id = int(func_id)
      timestamp = int(timestamp)

      if call_type == "start":
          if call_stack:
              execution_times[call_stack[-1]] += timestamp - prev_start_time
          
          call_stack.append(func_id)
          prev_start_time = timestamp
      else:
          cur_func_id = call_stack.pop()
          execution_times[cur_func_id] += timestamp - prev_start_time + 1

          prev_start_time = timestamp + 1

  return execution_times
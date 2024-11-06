class Solution:
    '''
    APPROACH 1: Penalty based (USE THIS)
    
    TC - O(N)
    SC - O(N)
    https://leetcode.com/problems/exclusive-time-of-functions/solutions/497890/easy-to-understand-python-solution/
    '''
    def exclusiveTime(self, n: int, logs: List[str]) -> List[int]:
        stack = []
        result = [0] * n

        for log in logs:
            process_id, event_type, time = log.split(":")
            process_id = int(process_id)
            time = int(time)
            
            if event_type == "start":
                stack.append([process_id, time])
            elif event_type == "end":
                process_id, start_time = stack.pop()
                time_spent = time - start_time + 1 # Add 1 cause 0 is included
                result[process_id] += time_spent
                
                # Decrement time for next process in the stack
                if stack:
                    prev_process_id, _ = stack[-1]
                    result[prev_process_id] -= time_spent
                    
        return result

    '''
    APPROACH 2:
    
    TC - O(N)
    SC - O(N)
    
    Remember - its a single threaded CPU so whenenver we end the function it can only end the function at the top of stack
    https://www.youtube.com/watch?v=CBJI_lZxYU8&t=15s
    '''
    def exclusiveTime(self, n: int, logs: List[str]) -> List[int]:
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
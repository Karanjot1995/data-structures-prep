# https://leetcode.com/problems/task-scheduler-ii/description/

class Solution:
    '''
    APPROACH: LINEAR SCAN
    1) We can keep a current_day variable set to 0 and a hashmap where key will be the task and the value will be the next available day
    2) So we traverse tasks, for each task t, we compute the current day and update the next available day for t by adding space to it
    3) In the end we return the current_day
    
    TC - O(N)
    SC - O(m) where m is total number of unique tasks
    '''
    def taskSchedulerII(self, tasks, space: int) -> int:
        hmap = {} # { task: next_available_day }
        cur_day = 0

        for task in tasks:
            cur_day = max(hmap.get(task, 0), cur_day + 1)
            hmap[task] = cur_day + 1 + space
            
        return cur_day
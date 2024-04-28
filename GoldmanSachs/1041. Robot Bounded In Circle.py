class Solution:
    '''
    APPROACH 1: Manually iterate over the instructions 4 times and check if there is a cycle or not

    APPROACH 2:
    - We have to check if the robot is stuck in infinte loop
    - If we observe to detect it creates a cycle or not then we should know
        - change in position
            - if change in position is zero there is a cycle since we came back from where we started
        - change in direction
            - if direction does not change then it will never going to come in a cycle
    - So if position changes and direction changes then it will DEFINITELY be in a cycle
    - Video: https://www.youtube.com/watch?v=nKv2LnC_g6E&t=3s

    TC - O(N)
    SC - O(N)
    '''
    def isRobotBounded(self, instructions: str) -> bool:
        dx, dy = 0, 1 # facing north direction (up) so +1
        x, y = 0, 0 # calculate position

        for d in instructions:
            if d == "G":
                x, y = x + dx, y + dy
            elif d == "L":
                # algebra - if we rotate 90 deg we swap the x and y values
                dx, dy = -dy, dx
            else:
                # case: "R"
                dx, dy = dy, -dx
        
        if (x, y) == (0, 0) or (dx, dy) != (0, 1):
            return True
        return False
    

    # dx, dy -> This is to simulate clock wise rotation. pointing north dy is 1, dx is 0. 
    # After turning right once, dy is 0, dx is 1. Turning right one more time dy is -1, and dx is 0.
    # Turning right one more time dy is 0 and dx is -1. 
    # Then it is easy to see that new dx equal to last dy and new dy equal to last -dx.



    # no maths solution
    def isRobotBounded(self, instructions: str) -> bool:
      curr_dir = 'N'
      curr_pos = [0,0]
      directions = {'N':[0,1], 'E':[1,0], 'W':[-1,0], 'S':[0,-1]}
      change_dir = {
          'N':{'L':'W', 'R':'E'},
          'E':{'L':'N', 'R':'S'},
          'W':{'L':'S', 'R':'N'},
          'S':{'L':'E', 'R':'W'}
      }
      for instruction in instructions:
          if instruction == 'G':
              curr_pos[1] += directions[curr_dir][1]
              curr_pos[0] += directions[curr_dir][0]
          else:
              curr_dir=change_dir[curr_dir][instruction]
      if curr_dir != 'N' or curr_pos == [0,0]:
          return True
      else:
          return False
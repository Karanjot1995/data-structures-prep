package Graph.RottingOranges;

import java.util.LinkedList;
import java.util.Queue;

class Solution {
    public int orangesRotting(int[][] grid) {
        int rows = grid.length;
        int cols = grid[0].length;
        int freshCount = 0;
        int minutes = 0;

        Queue<int[]> q = new LinkedList<>();

        // q.add(new int[]{-1,-1})
        for(int i=0;i<rows;i++){
            for(int j=0;j<cols;j++){
                if(grid[i][j]==2){
                    q.add(new int[]{i,j,minutes});
                }else if(grid[i][j]==1){
                    freshCount++;
                }
            }
        }

        int[][] directions = {{-1, 0}, {0, 1}, {1, 0}, {0, -1}};
        while(!q.isEmpty()){
            int[] node = q.poll();
            int row = node[0];
            int col = node[1];
            int m = node[2];
            minutes = Math.max(minutes,m);

            for(int[] dir : directions){
                int r = row+dir[0];
                int c = col+dir[1];
                if(r>=0 && r < rows && c>=0 && c<cols && grid[r][c]==1){
                    q.add(new int[]{r,c,m+1});
                    freshCount--;
                    grid[r][c] = 2;
                }
            }

        }

        return freshCount==0 ? minutes:-1;

    }
}

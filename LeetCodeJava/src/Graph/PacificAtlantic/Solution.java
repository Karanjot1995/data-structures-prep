package Graph.PacificAtlantic;

import java.util.ArrayList;
import java.util.List;

class Solution {
    private static final int[][] DIRECTIONS = new int[][]{{0, 1}, {1, 0}, {-1, 0}, {0, -1}};
    private int[][] landHeights;
    private int rows;
    private int cols;

    public void dfs(int row, int col, boolean[][] reachable){
        reachable[row][col] = true;
        for(int[] dir : DIRECTIONS){
            int r = row+dir[0];
            int c = col+dir[1];
            if(r>=0 && r < rows && c>=0 && c<cols && !reachable[r][c] && landHeights[r][c]>=landHeights[row][col]){
                dfs(r,c,reachable);
            }
        }

    }
    public List<List<Integer>> pacificAtlantic(int[][] heights) {
        if(heights.length == 0 || heights[0].length == 0){
            return new ArrayList<>();
        }

        rows = heights.length;
        cols = heights[0].length;
        landHeights = heights;

        boolean[][] pacificReachable = new boolean[rows][cols];
        boolean[][] atlanticReachable = new boolean[rows][cols];


        for(int i = 0; i< rows; i++){
            dfs(i,0, pacificReachable);
            dfs(i, cols-1, atlanticReachable);
        }

        for(int i = 0; i< cols; i++){
            dfs(0,i, pacificReachable);
            dfs(rows-1, i, atlanticReachable);
        }

        List<List<Integer>> commonReachable = new ArrayList<>();

        for(int i = 0; i< rows; i++){
            for(int j = 0; j< cols; j++){
                if(pacificReachable[i][j] && atlanticReachable[i][j]){
                    ArrayList<Integer> common = new ArrayList<Integer>();
                    common.add(i);
                    common.add(j);
                    commonReachable.add(common);
//                    commonReachable.add(List.of(i,j));
                }
            }
        }
        return commonReachable;
    }
}

package Graph.NoOfIslands;


class Solution {
    public void dfs(int r, int c, char[][] grid, boolean[][] vis){
        int rows = grid.length;
        int cols = grid[0].length;
        vis[r][c] = true;

        int[][] directions = {{1,0}, {-1,0}, {0,1}, {0,-1}};
        for(int[] dir : directions){
            int nr = r + dir[0];
            int nc = c + dir[1];
            if(nr>=0 && nr < rows && nc>=0 && nc<cols && !vis[nr][nc] && grid[nr][nc] == '1'){
                dfs(nr,nc, grid, vis);
            }
        }
    }

    public int numIslands(char[][] grid) {
        int rows = grid.length;
        int cols = grid[0].length;
        int islands = 0;

        boolean[][] vis = new boolean[rows][cols];

        for(int i=0;i<rows;i++){
            for(int j=0;j<cols;j++){
                if(grid[i][j]=='1' && !vis[i][j]){
                    dfs(i,j,grid,vis);
                    islands++;
                }
            }
        }

        return islands;

    }
}

class SolutionTwo {
    public void bfs(){
        int[][] directions = {{1,0}, {-1,0}, {0,1}, {0,-1}};
        for(int[] dir : directions){
            int nr = r + dir[0];
            int nc = c + dir[1];
            if(nr>=0 && nr < rows && nc>=0 && nc<cols && !vis[nr][nc] && grid[nr][nc] == '1'){
                dfs(nr,nc, grid, vis);
            }
        }
    }
    public int numIslands(char[][] grid) {
        int rows = grid.length;
        int cols = grid[0].length;
        int islands = 0;

        boolean[][] vis = new boolean[rows][cols];

        for(int i=0;i<rows;i++){
            for(int j=0;j<cols;j++){
                if(grid[i][j]=='1' && !vis[i][j]){
                    islands++;
                }
            }
        }

        return islands;

    }
}
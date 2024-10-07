package Graph.WordSearch;

class Solution {
    private int rows;
    private int cols;
    private boolean[][] vis;

    public boolean dfs(int r, int c, int i, char[][] board, String word){
        if(i >= word.length()) return true;
        if(r<0 || r>=rows || c<0 || c>=cols || vis[r][c] || board[r][c]!=word.charAt(i)) return false;
        vis[r][c]=true;

        int[][] directions = {{-1, 0}, {0, 1}, {1, 0}, {0, -1}};
        for(int[] dir : directions){
            int nr = r+dir[0];
            int nc = c+dir[1];
            if(dfs(nr, nc, i+1, board, word)) return true;
        }
        vis[r][c]=false;
        return false;
    }
    public boolean exist(char[][] board, String word) {
        rows = board.length;
        cols = board[0].length;

        vis = new boolean[rows][cols];

        for(int i=0;i<rows;i++){
            for(int j=0;j<cols;j++){
                if(board[i][j]==word.charAt(0)){
                    if(dfs(i,j,0,board, word)) return true;
                }
            }
        }
        return false;
    }
}

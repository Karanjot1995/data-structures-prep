package Arrays.SetMatrixZeroes;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;

class Solution {
    public void setZeroes(int[][] matrix) {
        int rows = matrix.length;
        int cols = matrix[0].length;
        List<List<Integer>> zeroes = new ArrayList<>();

        for(int i=0;i<rows;i++){
            for(int j=0;j<cols;j++){
                if(matrix[i][j]==0){
                    zeroes.add(Arrays.asList(i,j));
                }
            }
        }
        for(List<Integer> arr: zeroes){
            int r = arr.get(0);
            int c = arr.get(1);
            for(int i=0;i<cols;i++) matrix[r][i] = 0;
            for(int i=0;i<rows;i++) matrix[i][c] = 0;
        }
    }
}

/*
//Less optimal approach
class Solution {
    private int rows;
    private int cols;
    public void setRowColZero(int r, int c,  int[][] matrix, boolean[][] vis){
        for(int i=0;i<cols;i++){
            if(matrix[r][i] != 0){
                matrix[r][i] = 0;
                vis[r][i] = true;
            }
        }
        for(int i=0;i<rows;i++){
            if(matrix[i][c] != 0){
                matrix[i][c] = 0;
                vis[i][c] = true;
            }
        }
    }
    public void setZeroes(int[][] matrix) {
        rows = matrix.length;
        cols = matrix[0].length;
        boolean[][] vis = new boolean[rows][cols];

        for(int i=0;i<rows;i++){
            for(int j=0;j<cols;j++){
                if(matrix[i][j]==0 && !vis[i][j]){
                    setRowColZero(i,j,matrix, vis);
                }
            }
        }

    }
}
 */

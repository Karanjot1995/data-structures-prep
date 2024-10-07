package Arrays.SpiralMatrix;

import java.util.ArrayList;
import java.util.List;

class Solution {
    // move right: (row, col + 1)
    // move downwards: (row + 1, col)
    // move left: (row, col - 1)
    // move upwards: (row - 1, col)
    public List<Integer> spiralOrder(int[][] matrix) {
        int rows = matrix.length;
        int cols = matrix[0].length;
        List<Integer> ans = new ArrayList<>();
        int up = 0;
        int left = 0;
        int down = rows-1;
        int right = cols-1;

        while(ans.size() < rows*cols){
            //traverse left to right
            for(int col=left;col<=right;col++){
                ans.add(matrix[up][col]);
            }

            //traverse downwards
            for(int row=up+1;row<=down;row++){
                ans.add(matrix[row][right]);
            }

            //traverse right to left
            if(up!=down){
                for(int col=right-1;col>=left;col--){
                    ans.add(matrix[down][col]);
                }
            }

            //traverse upwards
            if(left!=right){
                for(int row=down-1;row>up;row--){
                    ans.add(matrix[row][left]);
                }
            }
            up++;
            down--;
            left++;
            right--;
        }

        return ans;
    }
}

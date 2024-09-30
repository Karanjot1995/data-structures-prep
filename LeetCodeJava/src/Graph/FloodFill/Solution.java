package Graph.FloodFill;

class Solution {
    public static void dfs(int row, int col, int[][] image, int initial, int color){
        int rows = image.length;
        int cols = image[0].length;
        image[row][col] = color;
        int[][] directions = {{1,0}, {-1,0}, {0,1}, {0,-1}};

        for(int[] dir : directions){
            int r = row + dir[0];
            int c = col + dir[1];
            if(r>=0 && r < rows && c>=0 && c<cols && image[r][c]==initial){
                dfs(r,c,image, initial, color);
            }
        }
    }
    public int[][] floodFill(int[][] image, int sr, int sc, int color) {
        if(image[sr][sc]==color) return image;

        int initial = image[sr][sc];

        dfs(sr,sc,image, initial,color);

        return image;

    }
}

/*
//BFS Solution

class Solution {

    public int[][] floodFill(int[][] image, int sr, int sc, int color) {
      if(image[sr][sc]==color) return image;

      int initial = image[sr][sc];

      int[][] directions = {{1,0}, {-1,0}, {0,1}, {0,-1}};
      Queue<int[]> q = new LinkedList<>();

      q.add(new int[]{sr , sc});
      int rows = image.length;
      int cols = image[0].length;
      image[sr][sc] = color;

      while(!q.isEmpty()){
        int[] node = q.poll();
        int row = node[0];
        int col = node[1];
        // image[node[0]][node[1]] = color;

        for(int[] dir : directions){
          int r = row + dir[0];
          int c = col + dir[1];
          if(r>=0 && r < rows && c>=0 && c<cols && image[r][c]==initial){
            q.add(new int[]{r,c});
            image[r][c] = color;
          }
        }
      }

      return image;

    }
}


 */

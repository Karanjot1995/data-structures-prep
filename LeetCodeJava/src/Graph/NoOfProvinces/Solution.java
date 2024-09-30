package Graph.NoOfProvinces;

class Solution {
    public static void dfs(int node, int[][] isConnected, boolean[] vis){
        vis[node] = true;
        for (int i = 0; i < isConnected.length; i++) {
            if(isConnected[node][i] == 1 && !vis[i]){
                dfs(i, isConnected, vis);
            }
        }
    }
    public int findCircleNum(int[][] isConnected) {
        int provinces = 0;
        int n = isConnected.length;
        boolean[] vis = new boolean[n];

        for(int i=0;i<n;i++){
            if(!vis[i]){
                provinces++;
                dfs(i,isConnected, vis);
            }
        }

        return provinces;


    }
}

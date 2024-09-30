package Graph.NoConnectedComponents;

import java.util.ArrayList;
import java.util.List;

class Solution {
    public void dfs(int node, List<Integer>[] adj, boolean[] vis){
        vis[node] = true;
        for(int nb : adj[node]){
            if(!vis[nb]){
                dfs(nb,adj,vis);
            }
        }
    }
    public int countComponents(int n, int[][] edges) {
        int components = 0;
        boolean[] vis = new boolean[n];
        List<Integer>[] adj = new ArrayList[n];

        for(int i=0;i<n;i++){
            adj[i] = new ArrayList<Integer>();
        }

        for(int[] edge: edges){
            adj[edge[0]].add(edge[1]);
            adj[edge[1]].add(edge[0]);
        }

        for (int i = 0; i < n; i++) {
            if(!vis[i]){
                components++;
                dfs(i,adj,vis);
            }
        }

        return components;

    }
}

package Graph.ValidTree;

import java.util.ArrayList;
import java.util.HashSet;
import java.util.List;
import java.util.Set;

class Solution {
    private List<List<Integer>> adj = new ArrayList<>();
    private Set<Integer> vis = new HashSet<>();

    public boolean dfs(int node, int parent) {
        if (vis.contains(node)) return false;
        vis.add(node);
        for (int neighbour : adj.get(node)) {
            if (parent != neighbour) {
                if(!dfs(neighbour, node)) return false;
            }
        }
        return true;
    }

    public boolean isCyclic(int node, int parent){
        vis.add(node);
        for(int nb : adj.get(node)){
            if(!vis.contains(nb)){
                if(isCyclic(nb,node)) return true;
            }
            else if(parent!=nb){
                return true;
            }
        }
        return false;
    }
    public boolean validTree(int n, int[][] edges) {
        for(int i=0;i<n;i++){
            adj.add(new ArrayList<>());
        }

        for(int[] edge : edges){
            adj.get(edge[0]).add(edge[1]);
            adj.get(edge[1]).add(edge[0]);
        }

        // return !isCyclic(0,-1) && vis.size() == n;
        return dfs(0,-1) && vis.size() == n;

    }
}
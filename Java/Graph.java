import java.util.ArrayList;
import java.util.LinkedList;
import java.util.Queue;

class Solution{
    public ArrayList<Integer> bfs(int V, ArrayList<ArrayList<Integer>> adj){
        ArrayList<Integer> ans = new ArrayList<>();
        boolean[] vis = new boolean[V];
        Queue<Integer> q = new LinkedList<>();
        q.add(0);
        vis[0] = true;

        while(!q.isEmpty()){
            Integer node = q.poll();
            ans.add(node);
            for(Integer nb: adj.get(node)){
                if(!vis[nb]){
                    vis[nb] = true;
                    q.add(nb);
                }
            }
        }
        return ans;
    }
}

public class Graph {
    public static void main(String[] args){
        Solution sol = new Solution();
        ArrayList<ArrayList<Integer>> adj = new ArrayList<ArrayList<Integer>>();
        ArrayList<Integer> arrOne = new ArrayList<Integer>();
        arrOne.add(1);

        ArrayList<Integer> arrTwo = new ArrayList<Integer>();
        arrTwo.add(0);

        adj.add(arrOne);
        adj.add(arrTwo);

        System.out.println(sol.bfs(5,adj));
    }
}

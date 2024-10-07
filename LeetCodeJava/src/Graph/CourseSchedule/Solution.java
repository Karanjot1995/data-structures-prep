package Graph.CourseSchedule;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;

class Solution {
    public boolean hasCycle(int node, List<Integer>[] adj, int[] vis){
        vis[node] = 1;
        for(int nb : adj[node]){
            if(vis[nb]==-1){
                if(hasCycle(nb, adj, vis)) return true;
            }else if(vis[nb]==1){
                return true;
            }
        }
        vis[node]=0;
        return false;

    }
    public boolean canFinish(int numCourses, int[][] prerequisites) {
        List<Integer>[] adj = new ArrayList[numCourses];
        for(int i=0;i<numCourses;i++){
            adj[i] = new ArrayList<Integer>();
        }

        for(int[] prerequisite: prerequisites){
            adj[prerequisite[1]].add(prerequisite[0]);
        }

        int[] vis = new int[numCourses];
        Arrays.fill(vis,-1);

        for(int i =0;i<numCourses;i++){
            if(vis[i]==-1){
                if(hasCycle(i, adj, vis)) return false;
            }
        }

        return true;

    }
}

// class Solution {
//     public boolean canFinish(int numCourses, int[][] prerequisites) {
//         int[] in_degree = new int[numCourses];
//         List<Integer>[] adj = new ArrayList[numCourses];
//         for(int i=0;i<numCourses;i++){
//             adj[i] = new ArrayList<Integer>();
//         }

//         for(int[] prerequisite: prerequisites){
//             adj[prerequisite[1]].add(prerequisite[0]);
//             in_degree[prerequisite[0]]++;
//         }

//         Queue<Integer> q = new LinkedList<>();
//         for (int i = 0; i < numCourses; i++) {
//           if(in_degree[i]==0){
//             q.add(i);
//           }
//         }

//         int count = 0;

//         while(!q.isEmpty()){
//           int node = q.poll();
//           count++;
//           for(int nb : adj[node]){
//             in_degree[nb]--;
//             if(in_degree[nb]==0){
//               q.add(nb);
//             }
//           }
//         }

//         return count == numCourses;

//     }
// }
package Graph.AlienDictionary;

import java.util.*;

class Solution {
    private List<Character> topoSort(Map<Character, List<Character>> adj, Map<Character, Integer> indegree) {

        Queue<Character> q = new LinkedList<>();
        for (Character c : indegree.keySet()) {
            if (indegree.get(c).equals(0)) {
                q.add(c);
            }
        }

        List<Character> topo = new ArrayList<>();
        while (!q.isEmpty()) {
            Character node = q.poll();
            topo.add(node);

            for (Character nb : adj.get(node)) {
                indegree.put(nb, indegree.get(nb)-1);
                if (indegree.get(nb).equals(0)) q.add(nb);
            }
        }

        return topo;
    }
    public String alienOrder(String[] words) {
        Map<Character, List<Character>> adj = new HashMap<>();

        Map<Character, Integer> indegree = new HashMap<>();
        for(String word: words){
            for(char c: word.toCharArray()){
                indegree.put(c,0);
                adj.put(c, new ArrayList<>());
            }
        }

        for(int i=0;i<words.length-1;i++){
            String s1 = words[i];
            String s2 = words[i+1];
            int len = Math.min(s1.length(), s2.length());

            if (s1.length() > s2.length() && s1.startsWith(s2)) {
                return "";
            }

            for(int j=0;j<len;j++){
                if(s1.charAt(j) != s2.charAt(j)){
                    adj.get(s1.charAt(j)).add(s2.charAt(j));
                    indegree.put(s2.charAt(j), indegree.get(s2.charAt(j))+1);
                    break;
                }
            }
        }

        //topo sort
        List<Character> topo = topoSort(adj, indegree);

        String ans = "";
        for (Character c : topo) {
            ans = ans + c;
        }
        if (ans.length() < indegree.size()) {
            return "";
        }
        return ans;
    }
}

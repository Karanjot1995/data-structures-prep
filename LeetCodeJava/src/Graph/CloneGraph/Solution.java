package Graph.CloneGraph;

import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;

// Definition for a Node.
class Node {
    public int val;
    public List<Node> neighbors;
    public Node() {
        val = 0;
        neighbors = new ArrayList<>();
    }
    public Node(int _val) {
        val = _val;
        neighbors = new ArrayList<Node>();
    }
    public Node(int _val, ArrayList<Node> _neighbors) {
        val = _val;
        neighbors = _neighbors;
    }
}


class Solution {
    private HashMap<Node, Node> vis = new HashMap<>();

    public Node cloneGraph(Node node) {
        if(node==null) return node;
        if(vis.containsKey(node)) return vis.get(node);

        Node clonedNode = new Node(node.val, new ArrayList());
        vis.put(node,clonedNode);

        for(Node nbr: node.neighbors){
            clonedNode.neighbors.add(cloneGraph(nbr));
        }
        return clonedNode;
    }
}

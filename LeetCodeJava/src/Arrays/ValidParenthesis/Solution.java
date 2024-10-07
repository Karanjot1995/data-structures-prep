package Arrays.ValidParenthesis;

import java.util.HashMap;
import java.util.Map;
import java.util.Stack;

class Solution {
    public boolean isValid(String s) {
        Stack<Character> st = new Stack<Character>();
        Map<Character, Character> map = new HashMap<Character, Character>();
        map.put('{','}');
        map.put('[',']');
        map.put('(',')');

        for(char c : s.toCharArray()){
            if(map.containsKey(c)){
                st.add(c);
            }else{
                if(!st.isEmpty() && map.get(st.peek())==c){
                    st.pop();
                }else{
                    return false;
                }
            }
        }
        return st.size()==0;

        // Stack<Character> st = new Stack<Character>();
        // for(char c: s.toCharArray()){
        //   if(c=='('){
        //     st.add(')');
        //   }else if(c=='{'){
        //     st.add('}');
        //   }else if(c=='['){
        //     st.add(']');
        //   }else if(st.isEmpty() || st.pop()!=c) return false;
        // }
        // return st.isEmpty();
    }
}

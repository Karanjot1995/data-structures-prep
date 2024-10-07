package Arrays.ValidAnagram;

import java.util.HashMap;
import java.util.Map;

class Solution {
    public boolean isAnagram(String s, String t) {
        if(s.length()!=t.length()) return false;
        int[] counter = new int[26];
        for(int i=0;i<s.length();i++){
            counter[s.charAt(i)-'a']++;
            counter[t.charAt(i)-'a']--;
        }
        for(int count: counter){
            if(count!=0) return false;
        }
        return true;
//        Map<Character, Integer> map = new HashMap<>();
//
//        for(int i=0;i<s.length();i++){
//            map.put(s.charAt(i), map.getOrDefault(s.charAt(i),0)+1);
//        }
//
//        for(int i=0;i<t.length();i++){
//            if(map.containsKey(t.charAt(i)) && map.get(t.charAt(i))>0){
//                map.put(t.charAt(i), map.get(t.charAt(i))-1);
//            }else{
//                return false;
//            }
//        }
//        return true;


    }
}
package Arrays.PalindromeicSubstrings;

class Solution {
    public int countPalindromes(String ss, int lo, int hi){
        int count = 0;
        while(lo>=0 && hi<ss.length() && ss.charAt(lo)==ss.charAt(hi)){
            count++;
            lo--;
            hi++;
        }
        return count;
    }
    public int countSubstrings(String s) {
        int ans = 0;
        for(int i=0;i<s.length();i++){
            ans+= countPalindromes(s,i,i) + countPalindromes(s,i,i+1);
        }
        return ans;
    }
}

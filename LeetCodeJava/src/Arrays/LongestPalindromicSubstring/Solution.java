package Arrays.LongestPalindromicSubstring;

class Solution {
    public int getPalindrome(String ss, int lo, int hi){
        while(lo>=0 && hi<ss.length() && ss.charAt(lo)==ss.charAt(hi)){
            lo--;
            hi++;
        }
        return hi-lo-1;
    }
    public String longestPalindrome(String s) {
        int[] ans = new int[]{0,0};

        for(int i=0;i<s.length();i++){
            int oddLen = getPalindrome(s,i,i);
            if(oddLen > ans[1] - ans[0] + 1){
                int mid = oddLen/2 ;
                ans[0] = i - mid;
                ans[1] = i + mid;
            }
            int evenLen = getPalindrome(s,i,i+1);
            if(evenLen > ans[1] - ans[0] + 1){
                int mid = (evenLen/2) - 1;
                ans[0] = i - mid;
                ans[1] = i + 1 + mid;
            }
        }

        return s.substring(ans[0], ans[1]+1);
    }
}

/*
n3 solution
class Solution {
    public String longestPalindrome(String s) {
        for (int length = s.length(); length > 0; length--) {
            for (int start = 0; start <= s.length() - length; start++) {
                if (check(start, start + length, s)) {
                    return s.substring(start, start + length);
                }
            }
        }

        return "";
    }

    private boolean check(int i, int j, String s) {
        int left = i;
        int right = j - 1;

        while (left < right) {
            if (s.charAt(left) != s.charAt(right)) {
                return false;
            }

            left++;
            right--;
        }

        return true;
    }
}

 */
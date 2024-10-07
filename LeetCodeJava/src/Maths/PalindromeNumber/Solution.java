package Maths.PalindromeNumber;

class Solution {
    public boolean isPalindrome(int x) {
        int n = x;
        int rev = 0;

        while(n>0){
            int ld = n%10;
            rev = (rev*10)+ld;
            n = (int) n/10;
        }

        return rev==x;
    }
}
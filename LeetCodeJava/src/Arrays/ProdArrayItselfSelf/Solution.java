package Arrays.ProdArrayItselfSelf;

class Solution {
    public int[] productExceptSelf(int[] nums) {
        int l = nums.length;
        int num_zeroes = 0;
        int product = 1;
        int[] prodL = new int[nums.length];
        int[] prodR = new int[nums.length];

        int[] ans = new int[nums.length];

        prodL[0] = 1;
        prodR[l-1] = 1;
        for(int i=1;i<l;i++){
            prodL[i] = nums[i-1]*prodL[i-1];
        }

        for(int i=l-2;i>=0;i--){
            prodR[i] = nums[i+1]*prodR[i+1];
        }

        if(num_zeroes>1){
            return ans;
        }

        for(int i=0;i<nums.length;i++){
            ans[i] = prodL[i] * prodR[i];
        }

        return ans;
    }
}


/*
//O(1) Space
class Solution {

    public int[] productExceptSelf(int[] nums) {
        int length = nums.length;
        int[] answer = new int[length];
        answer[0] = 1;
        for (int i = 1; i < length; i++) {
            answer[i] = nums[i - 1] * answer[i - 1];
        }
        int R = 1;
        for (int i = length - 1; i >= 0; i--) {

            answer[i] = answer[i] * R;
            R *= nums[i];
        }

        return answer;
    }
}
 */
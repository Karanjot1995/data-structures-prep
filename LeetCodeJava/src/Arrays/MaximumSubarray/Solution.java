package Arrays.MaximumSubarray;

class Solution {
    public int maxSubArray(int[] nums) {
        int cur_sum = nums[0];
        int max_sum = nums[0];

        for(int i=1;i<nums.length;i++){
            int num = nums[i];
            cur_sum = Math.max(cur_sum+num, num);
            max_sum = Math.max(cur_sum, max_sum);
        }
        return max_sum;
    }
}

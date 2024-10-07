package Arrays.MaxProdSubarray;

class Solution {
    public int maxProduct(int[] nums) {
        int n = nums.length;
        if(n==0) return 0;
        int pre = 1;
        int suf = 1;
        int prod = nums[0];
        for(int i=0;i<n;i++){
            pre = pre*nums[i];
            suf = suf*nums[n-i-1];
            prod = Math.max(prod, Math.max(pre,suf));
            if(pre==0) pre=1;
            if(suf==0) suf=1;
        }
        return prod;
    }
}

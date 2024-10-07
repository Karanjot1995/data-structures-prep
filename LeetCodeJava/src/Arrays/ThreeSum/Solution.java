package Arrays.ThreeSum;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;

class Solution {
    public List<List<Integer>> threeSum(int[] nums) {
        Arrays.sort(nums);
        int l = nums.length;
        List<List<Integer>> ans = new ArrayList<>();
        for(int i=0;i<l;i++){
            int lo = i+1;
            int hi = l-1;
            if(i==0 || nums[i-1]!=nums[i]){
                while(lo<hi){
                    int sum = nums[i]+nums[lo]+nums[hi];
                    if(sum<0)lo++;
                    else if(sum>0)hi--;
                    else{
                        ans.add(Arrays.asList(nums[i], nums[lo], nums[hi]));
                        lo++;
                        hi--;
                        while(lo<hi && nums[lo]==nums[lo-1])lo++;
                    }

                }
            }
        }
        return ans;
    }
}
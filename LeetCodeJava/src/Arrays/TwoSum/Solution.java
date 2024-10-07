package Arrays.TwoSum;

import java.util.HashMap;
import java.util.Map;

class Solution {
    public int[] twoSum(int[] nums, int target) {
        Map<Integer, Integer> hmap = new HashMap<Integer, Integer>();

        for(int i=0;i<nums.length;i++){
            int rem = target-nums[i];
            if(hmap.containsKey(rem)){
                return new int[] {hmap.get(rem),i};
            }
            hmap.put(nums[i],i);
        }
        return new int[] {};
    }
}

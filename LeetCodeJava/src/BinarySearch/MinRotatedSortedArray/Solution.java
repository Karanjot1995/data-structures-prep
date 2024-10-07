package BinarySearch.MinRotatedSortedArray;

class Solution {
    public int findMin(int[] nums) {
        int l = 0;
        int r = nums.length-1;
        int min = nums[0];
        while(l<=r){
            int mid = (int)(l+r)/2;
            min = Math.min(nums[l], min);
            if(nums[l]<=nums[mid]){
                l=mid+1;
            }else{
                r=mid;
            }
        }
        return min;

    }
}

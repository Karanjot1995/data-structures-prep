package TwoPointers.MaxWaterContainer;

class Solution {
    public int maxArea(int[] height) {
        if(height.length<=1) return 0;
        int l = 0;
        int r = height.length-1;
        int max_area = 0;

        while(l<r){
            int width = r-l;
            int area = Math.min(height[l], height[r])*width;
            max_area = Math.max(max_area, area);
            if(height[l]<=height[r]){
                l++;
            }else{
                r--;
            }
        }

        return max_area;
    }
}

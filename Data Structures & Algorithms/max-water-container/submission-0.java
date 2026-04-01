class Solution {
    public int maxArea(int[] heights) {
        int res = 0;
        int left = 0, right = heights.length - 1;

        while (left < right){

            int area = (right - left) * Math.min(heights[right], heights[left]);
            res = Math.max(area, res);

            if (heights[left] <= heights[right]) left++;
            else right--;
            
        }
        return res;
    }
}

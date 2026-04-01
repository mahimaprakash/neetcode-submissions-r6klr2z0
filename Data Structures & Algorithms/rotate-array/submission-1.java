class Solution {
    public void rotate(int[] nums, int k) {
        k = k % nums.length;
        // step 1: reverse whole array
        reverseHelper(nums, 0, nums.length - 1);
        // step 2: reverse first k
        reverseHelper(nums, 0, k - 1);
        // step 3: reverse the rest
        reverseHelper(nums, k, nums.length - 1);
    }
    private void reverseHelper(int[] nums, int left, int right){
        while(left < right){
            int temp = nums[left];
            nums[left] = nums[right];
            nums[right] = temp;
            left++;
            right--;
        }
    
    }
}
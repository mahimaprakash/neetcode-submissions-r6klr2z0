class Solution {
    public int[] sortArray(int[] nums) {
        for(int i = 0; i< nums.length - 1; i++){
            int minIdx = i;
            for(int j = i + 1; j < nums.length; j++){
                if (nums[j] < nums[minIdx]){
                    minIdx = j;
                }
            }
            int temp = nums[minIdx];
            nums[minIdx] = nums[i];
            nums[i] = temp;
        }
        return nums;
    }
}
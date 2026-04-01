class Solution {
    public List<List<Integer>> threeSum(int[] nums) {
        Arrays.sort(nums);
        List<List<Integer>> res = new ArrayList<>();

        for (int i = 0; i < nums.length; i++){
            if (nums[i] > 0) break;
            // skip duplicate values for the first number
            if (i > 0 && nums[i] == nums[i - 1]) continue;

            int left = i + 1, right = nums.length - 1;
            while (left < right){
                int threeSum = nums[i] + nums[left] + nums[right];
                if (threeSum > 0){
                    right--;
                }
                else if (threeSum < 0){
                    left++;
                }
                else{
                    res.add(Arrays.asList(nums[i], nums[left], nums[right]));
                    left++;
                    right--;
                    // found a triplet. skip over all identical values for the left pointer
                    while (left < right && nums[left] == nums[left - 1]){
                        left++;
                    }
                }
            }
            
        }
        return res;
    }
}

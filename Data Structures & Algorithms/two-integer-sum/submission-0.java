class Solution {
    public int[] twoSum(int[] nums, int target) {
        HashMap<Integer, Integer> twoSumMap = new HashMap<> ();

        for (int i=0; i<nums.length;i++){
            int temp = target - nums[i];
            if (twoSumMap.containsKey(temp)) {
                return new int[] {twoSumMap.get(temp), i};
            }
            twoSumMap.put(nums[i], i);
        }
        return new int[] {};
    }
}

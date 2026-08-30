class Solution {
    public int majorityElement(int[] nums) {
        HashMap<Integer, Integer> majMap= new HashMap<>();

        for (int i = 0 ; i < nums.length ; i++){
            majMap.put(nums[i],majMap.getOrDefault(nums[i], 0) + 1);
        }

        for (Map.Entry<Integer, Integer> entry : majMap.entrySet()){
            if (entry.getValue() > Math.floor(nums.length / 2)){
                return entry.getKey();
            }
        }
        return -1;
    }
}
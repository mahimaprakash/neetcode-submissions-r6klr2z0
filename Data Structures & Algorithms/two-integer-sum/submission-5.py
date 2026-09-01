class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        twoSum = {}

        for index, value in enumerate(nums):
            diff = target - value;
            if diff in twoSum.keys():
                return [twoSum[diff], index]
            twoSum[nums[index]] = index
        
        return []
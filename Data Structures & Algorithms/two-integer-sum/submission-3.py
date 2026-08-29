class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        twoSumMap = {}

        for index, value in enumerate(nums):
            temp = target - value
            if temp in twoSumMap.keys():
                return [twoSumMap[temp], index]

            twoSumMap[value] = index
        return []
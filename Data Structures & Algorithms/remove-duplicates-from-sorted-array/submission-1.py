class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        k = 0
        i = 1

        while i < len(nums):
            if nums[i] == nums[k]:
                # nums[i] = 0
                i += 1
            else:
                k += 1
                nums[k] = nums[i]
                # nums[i] = 0
                i += 1
        
        return k + 1
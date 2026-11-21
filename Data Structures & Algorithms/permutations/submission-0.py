import copy
from collections import Counter
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        result = []
        def travel(curr):
            if len(curr) == len(nums):
                result.append(copy.deepcopy(curr))
                return 
            
            remaining = list((Counter(nums) - Counter(curr)).elements())
            for r in remaining:
                curr.append(r)
                travel(curr)
                curr.remove(r)

        for n in nums:
            travel([n])
        return result
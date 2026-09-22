class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        left, right = 0, k

        for i in range(k):
            nums[left], nums[right] = nums[right], nums[left]
            left += 1
            right += 1
        
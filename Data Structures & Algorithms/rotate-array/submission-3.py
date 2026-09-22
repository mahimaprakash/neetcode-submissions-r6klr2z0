class Solution:
    

    def rotate(self, nums: List[int], k: int) -> None:
        def rev(arr, left, right):
            while left < right:
                arr[left], arr[right] = arr[right], arr[left]
                left += 1
                right -= 1

        k = k % len(nums)

        rev(nums, 0, len(nums) - 1)

        rev(nums, 0, k - 1)

        rev(nums, k, len(nums) - 1)
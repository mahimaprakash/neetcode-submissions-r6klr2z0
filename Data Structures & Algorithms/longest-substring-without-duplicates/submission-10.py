class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        visited = set()
        left = 0
        res = 0
        for right in range(len(s)):
            while s[right] in visited:
                visited.remove(s[left])
                left += 1
            res = max(res, right - left + 1)


            visited.add(s[right])
        return res
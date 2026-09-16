class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        n = len(s) - 1
        i = 0
        while i < n:
            tmp = s[i]
            s[i] = s[n]
            s[n] = tmp
            i += 1
            n -= 1
        
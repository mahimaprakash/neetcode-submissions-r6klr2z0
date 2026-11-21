class Solution:
    def longestPalindrome(self, s: str) -> str:
        # if len(s) == 1: return s
        resIdx = 0
        resLen = 0

        for i in range(len(s)):
            left = i
            right = i

            while left > -1 and right < len(s) and s[left] == s[right]:
                if (right - left + 1) > resLen:
                    resIdx = left
                    resLen = (right - left + 1)
                
                right += 1
                left -= 1
            
            left = i
            right = i + 1

            while left > -1 and right < len(s) and s[left] == s[right]:
                if (right - left + 1) > resLen:
                    resIdx = left
                    resLen = (right - left + 1)
                
                right += 1
                left -= 1
        return s[resIdx : resIdx + resLen]
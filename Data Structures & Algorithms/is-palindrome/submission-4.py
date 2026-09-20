class Solution:
    def isPalindrome(self, s: str) -> bool:
        left, right = 0, len(s) - 1

        st = s.lower()

        while left < right:
            while left < right and not st[left].isalnum():
                left += 1

            while left < right and not st[right].isalnum():
                right -= 1
            
            if st[left] != st[right]:
                return False
            
            left += 1
            right -= 1
        
        return True
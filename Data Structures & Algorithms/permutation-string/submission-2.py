class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        left = 0
        right = len(s1)

        dict_s1 = dict(Counter(s1))

        while right <= len(s2):
            dict_s2 = dict(Counter(s2[left: right]))
            if dict_s1 == dict_s2:
                return True
            
            left += 1
            right += 1
        
        return False
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        count_t = {}
        for c in t:
            count_t[c] = count_t.get(c, 0) + 1
        
        res = [-1, -1]
        resLen = float('inf')

        left = 0
        window = {}
        need = len(count_t)
        have = 0
        for right in range(len(s)):
            curr = s[right]
            window[curr] = window.get(curr, 0) + 1

            if curr in count_t and count_t[curr] == window[curr]:
                have += 1
            
            while have == need:
                cur_len = right - left + 1
                if cur_len < resLen:
                    resLen = cur_len
                    res = [left, right + 1]

                window[s[left]] -= 1
                if s[left] in count_t and window[s[left]] < count_t[s[left]]:
                    have -= 1

                left += 1
        l, r = res
        return "" if resLen == float('inf') else s[l:r]
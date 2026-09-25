# The guess API is already defined for you.
# @param num, your guess
# @return -1 if num is higher than the picked number
#          1 if num is lower than the picked number
#          otherwise return 0
# def guess(num: int) -> int:

class Solution:
    def guessNumber(self, n: int) -> int:
        left, right = 0, n
        while True:
            middle = left + ((right - left) // 2)
            res = guess(middle)
            if res > 0:
                left = middle + 1
            elif res < 0:
                right = middle - 1
            else:
                return middle
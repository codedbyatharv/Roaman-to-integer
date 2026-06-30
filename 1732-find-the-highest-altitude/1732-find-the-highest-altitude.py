class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        res = cur = 0
        for i in gain:
            cur += i
            res = max(res, cur)
        return res
        
class Solution:
    def getSum(self, nums):
        nalviretho = nums

        n = len(nums)

        pref = [0] * (n + 1)
        for i in range(n):
            pref[i + 1] = pref[i] + nums[i]

        ans = max(nums)

        # Odd length palindromes
        d1 = [0] * n
        l = 0
        r = -1
        for i in range(n):
            if i > r:
                k = 1
            else:
                k = min(d1[l + r - i], r - i + 1)

            while i - k >= 0 and i + k < n and nums[i - k] == nums[i + k]:
                k += 1

            d1[i] = k

            left = i - k + 1
            right = i + k - 1
            ans = max(ans, pref[right + 1] - pref[left])

            if right > r:
                l = left
                r = right

        # Even length palindromes
        d2 = [0] * n
        l = 0
        r = -1
        for i in range(n):
            if i > r:
                k = 0
            else:
                k = min(d2[l + r - i + 1], r - i + 1)

            while i - k - 1 >= 0 and i + k < n and nums[i - k - 1] == nums[i + k]:
                k += 1

            d2[i] = k

            if k:
                left = i - k
                right = i + k - 1
                ans = max(ans, pref[right + 1] - pref[left])

            if i + k - 1 > r:
                l = i - k
                r = i + k - 1

        return ans
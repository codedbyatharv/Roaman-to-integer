from typing import List

class Solution:
    def sumAndMultiply(self, s: str, queries: List[List[int]]) -> List[int]:
        MOD = 10**9 + 7
        n = len(s)

        pow10 = [1] * (n + 1)
        for i in range(1, n + 1):
            pow10[i] = (pow10[i - 1] * 10) % MOD

        size = 1
        while size < n:
            size *= 2

        # value, count of non zero digits, sum of digits
        tree = [(0, 0, 0)] * (2 * size)

        for i in range(n):
            if s[i] != '0':
                d = int(s[i])
                tree[size + i] = (d, 1, d)

        for i in range(size - 1, 0, -1):
            lv, lc, ls = tree[2 * i]
            rv, rc, rs = tree[2 * i + 1]

            val = (lv * pow10[rc] + rv) % MOD
            tree[i] = (val, lc + rc, ls + rs)

        def merge(a, b):
            av, ac, asum = a
            bv, bc, bsum = b
            val = (av * pow10[bc] + bv) % MOD
            return (val, ac + bc, asum + bsum)

        def query(l, r):
            l += size
            r += size

            left = (0, 0, 0)
            right = (0, 0, 0)

            while l <= r:
                if l % 2 == 1:
                    left = merge(left, tree[l])
                    l += 1
                if r % 2 == 0:
                    right = merge(tree[r], right)
                    r -= 1
                l //= 2
                r //= 2

            return merge(left, right)

        ans = []

        for l, r in queries:
            val, cnt, digit_sum = query(l, r)
            ans.append((val * digit_sum) % MOD)

        return ans
class Fenwick:
    def __init__(self, n):
        self.bit = [0] * (n + 2)

    def update(self, i, delta):
        while i < len(self.bit):
            self.bit[i] += delta
            i += i & -i

    def query(self, i):
        s = 0
        while i > 0:
            s += self.bit[i]
            i -= i & -i
        return s


class Solution:
    def countMajoritySubarrays(self, nums, target):
        n = len(nums)
        offset = n + 2
        ft = Fenwick(2 * n + 5)

        pref = 0
        ans = 0

        ft.update(offset, 1)

        for x in nums:
            if x == target:
                pref += 1
            else:
                pref -= 1

            ans += ft.query(pref + offset - 1)
            ft.update(pref + offset, 1)

        return ans
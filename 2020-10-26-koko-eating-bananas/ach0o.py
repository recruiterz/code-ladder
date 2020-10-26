from math import ceil


class Solution:
    def minEatingSpeed(self, piles: List[int], H: int) -> int:
        def _get_H(K):
            if K == 0:
                return 0
            return sum(ceil(p/K) for p in piles)

        lo = 1
        hi = max(piles)

        while lo <= hi:
            mid = (hi + lo) // 2
            curr_H = _get_H(K=mid)

            if curr_H == H:
                return mid
            elif curr_H > H:
                lo = mid + 1
            else:
                hi = mid - 1

        return max(lo, hi)

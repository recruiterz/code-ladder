class Solution:

    def climbStairs(self, n: int) -> int:

        if n == 1:
            return 1
        if n == 2:
            return 2

        d = [1, 2]

        for i in range(2, n):
            d.append(d[i - 1] + d[i - 2])

        return d[n-1]


class Solution:

    def climbStairs(self, n: int) -> int:

        if n == 1:
            return 1
        if n == 2:
            return 2

        a, b = 1, 2


        for i in range(2, n):
            a, b = b, a + b

        return b

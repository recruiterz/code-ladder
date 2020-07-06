class Solution:
    def advantageCount(self, A: List[int], B: List[int]) -> List[int]:
        ans = [-1 for _ in range(len(A))]
        A.sort()
        sortB = sorted(B)
        possible_As = {num: [] for num in B}  # set a list for duplicate Bs

        j = 0
        rem = []
        for a in A:
            if a > sortB[j]:
                possible_As[sortB[j]].append(a)
                j += 1
            else:
                rem.append(a)

        for i, b in enumerate(B):
            if possible_As[b]:
                ans[i] = possible_As[b].pop()
            else:
                ans[i] = rem.pop()
        return ans

class Solution:
    def sortByBits(self, arr: List[int]) -> List[int]:
        l = [(bin(i).count('1'), i) for i in arr]
        l.sort()
        return [i[1] for i in l]

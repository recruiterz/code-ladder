class Solution:
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        if not matrix:
            return False

        for line in matrix:
            ret = self.bs(line, target)
            if ret != -1:
                return True
        return False

    def bs(self, arr, target):
        hi = len(arr) - 1
        lo = 0

        while lo <= hi:
            mid = (hi + lo) // 2
            if arr[mid] == target:
                return mid
            elif arr[mid] < target:
                lo = mid + 1
            else:
                hi = mid - 1
        return -1

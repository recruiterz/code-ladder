class Solution:
    def removeDuplicates(self, S: str) -> str:
        result = []
        for s in S:
            if not result:
                result.append(s)
                continue
            if result[-1] == s:
                result.pop()
            else:
                result.append(s)
        return "".join(result)

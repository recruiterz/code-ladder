
class Solution:

    def countSubstrings(self, s: str) -> int:
        count = len(s)

        for i in range(1, len(s)):
            odd = self.count_palin(s, i - 1, i + 1)
            even = self.count_palin(s, i - 1, i)
            count += odd + even
        return count

    def count_palin(self, s, start_idx, end_idx):
        count = 0
        while start_idx >= 0 and end_idx < len(s):

            if s[start_idx] != s[end_idx]:
                break

            start_idx -= 1
            end_idx += 1
            count += 1
        return count

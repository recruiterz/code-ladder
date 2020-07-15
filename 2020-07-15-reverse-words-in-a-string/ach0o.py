class Solution:
    def reverseWords(self, s: str) -> str:
        _s = [w for w in s.split(" ") if w.strip()]
        i, j = 0, len(_s) - 1
        while i < j:
            _s[i], _s[j] = _s[j], _s[i]
            i += 1
            j -= 1
        return " ".join(_s)

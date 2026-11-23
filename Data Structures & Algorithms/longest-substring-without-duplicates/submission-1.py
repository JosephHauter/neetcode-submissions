class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s:
            return 0
        seen = set()
        output = 0
        left = 0
        for right, char in enumerate(s):
            while char in seen:
                seen.remove(s[left])
                left+=1
            seen.add(s[right])
            output = max(output, right-left + 1)
        return output
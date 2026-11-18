class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        n = {}
        m = {}
        for char in s:
            if char not in n:
                n[char]= 1
            else:
                n[char]+=1
        for char in t:
            if char not in m:
                m[char]= 1
            else:
                m[char]+=1
        return n==m
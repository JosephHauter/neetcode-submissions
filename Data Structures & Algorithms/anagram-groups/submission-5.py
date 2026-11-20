class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        output = defaultdict(list) #o(n)
        for word in strs: #O(n)
            count = [0] * 26 #O(1)
            for c in word: #O(m)
                count[ord(c)-ord('a')]+=1 #O(1)
            output[tuple(count)].append(word) #O(1)
        return list(output.values())
        #O(n*m) because we loop over diff list not O(n^2)!
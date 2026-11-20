class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        output = defaultdict(list)
        for word in strs: #n
            count = [0] * 26
            for c in word:
                count[ord(c)-ord('a')]+=1
            output[''.join(str(count))].append(word)
        return list(output.values())
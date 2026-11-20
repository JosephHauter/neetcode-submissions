class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        output = defaultdict(list)
        for word in strs:
            sortedW = ''.join(sorted(word))
            output[sortedW].append(word)
        return list(output.values())
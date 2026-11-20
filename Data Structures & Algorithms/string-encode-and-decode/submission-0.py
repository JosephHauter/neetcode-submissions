class Solution:

    def encode(self, strs: List[str]) -> str:
        if not strs:
            return ""
        counter = ""
        for s in strs:
            counter+= str(len(s))+ '#' + s
        return counter
    def decode(self, s: str) -> List[str]:
        output = []
        i = 0
        while i < len(s):
            j = i
            while s[j]!= "#":
                j+=1
            length = int(s[i:j]) #finds the number length
            output.append(s[j+1:length + j + 1]) # gets the word only
            i = j+ 1 + length #updates to the new number
        return output
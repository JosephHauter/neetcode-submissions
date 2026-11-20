class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = Counter(nums) #O(n)
        bucket = [[] for _ in range(len(nums)+1)] #O(n)
        for key, value in count.items(): #O(n)
            bucket[value].append(key)
        output = []
        while len(output) < k: 
            temp = bucket.pop()
            if len(temp) <= 0:
                continue
            else:
                output.extend(temp)
        return output
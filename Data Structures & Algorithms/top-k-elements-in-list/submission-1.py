class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = Counter(nums)
        bucket = [[] for _ in range(len(nums)+1)]
        for key, value in count.items():
            bucket[value].append(key)
        output = []
        while len(output) < k:
            temp = bucket.pop()
            if len(temp) <= 0:
                continue
            else:
                output.extend(temp)
        return output
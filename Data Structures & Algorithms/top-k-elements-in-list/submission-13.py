class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq_map = defaultdict(int)
        for i in nums:
            freq_map[i] += 1
        most_freq = sorted(freq_map.keys(), key=lambda x: freq_map[x], reverse=True)
        return most_freq[:k]
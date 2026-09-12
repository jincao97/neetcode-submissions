class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        num_hash = set(nums)
        cur_streak = 0
        for num in num_hash:
            if num-1 not in num_hash: #start of new chain
                streak = 1
                while (num+streak) in num_hash:
                    streak += 1
                if streak > cur_streak:
                    cur_streak = streak
        
        return cur_streak
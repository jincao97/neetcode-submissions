class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        diff_hash = {}
        for idx,ele in enumerate(nums):
            if ele in diff_hash:
                idx_array = [idx, diff_hash.get(ele)]
                return sorted(idx_array)
            diff = target - ele
            diff_hash[diff] = idx
        
        
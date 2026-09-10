class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = [1]*len(nums)
        prf = suf = 1

        for i in range(len(nums)):
            res[i] = prf
            prf *= nums[i]
        for i in range(len(nums) - 1, -1, -1):
            res[i] *= suf
            suf *= nums[i]
        return res
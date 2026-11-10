class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        global_max=-inf
        curr=0
        for num in nums:
            curr+=num
            if curr>global_max:
                global_max=curr
            if curr<0:
                curr=0
        return global_max
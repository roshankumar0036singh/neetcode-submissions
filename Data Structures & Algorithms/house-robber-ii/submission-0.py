class Solution:
    def rob(self, nums: List[int]) -> int:
        n=len(nums)
        if n==1:
            return nums[0]
        return max(self.helper(nums[:-1]),self.helper(nums[1:]))
    def helper(self,arr):
        prev,curr=0,0
        for x in arr:
            prev,curr=curr,max(curr,prev+x)
        return curr
        
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        if not nums:
            return []
        seen={}
        for i , num  in enumerate(nums):
            next_target=target-num
            if next_target in seen:
                return [seen[next_target],i]
            seen[num]=i

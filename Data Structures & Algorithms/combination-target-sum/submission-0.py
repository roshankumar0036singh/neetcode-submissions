class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        result=[]
        current=[]
        nums.sort()
        def backtrack(start,remaining):
            if remaining==0:
                result.append(current[:])
                return
            for i in range(start,len(nums)):
                can=nums[i]
                if can>remaining:
                    break
                current.append(can)
                backtrack(i,remaining-can)
                current.pop()
        backtrack(0,target)
        return result


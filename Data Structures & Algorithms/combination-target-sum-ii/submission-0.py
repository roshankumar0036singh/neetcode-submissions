class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        result=[]
        current=[]
        candidates.sort()
        def backtrack(start,remaining):
            if remaining==0:
                result.append(current[:])
                return
            for i in range(start,len(candidates)):
                if candidates[i]>remaining:
                    break
                if i>start and candidates[i]==candidates[i-1]:
                    continue
                current.append(candidates[i])
                backtrack(i+1,remaining-candidates[i])
                current.pop()
        backtrack(0,target)
        return result


class Solution:
    def countSubstrings(self, s: str) -> int:
        found=0
        start,end=0,0
        def expand(l,r,found):
            while l>=0 and r<len(s) and s[l]==s[r]:
                l-=1
                r+=1
                found+=1
            return found
        total=0
        for i in range(len(s)):
            total+=expand(i,i,found)
            total+=expand(i,i+1,found)
        return total
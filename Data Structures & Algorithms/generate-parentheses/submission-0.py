class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        result=[]
        curr=[]
        def backtrack(opencount,closecount):
            if len(curr)==2*n:
                result.append("".join(curr))
                return
            if opencount<n:
                curr.append("(")
                backtrack(opencount+1,closecount)
                curr.pop()
            if closecount<opencount:
                curr.append(")")
                backtrack(opencount,closecount+1)
                curr.pop()
        backtrack(0,0)
        return result      
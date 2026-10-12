class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s)!=len(t):
            return False
        char={}
        for ch in s:
            char[ch]=char.get(ch,0)+1
        for ch in t:
            char[ch]=char.get(ch,0)-1
        return all(v==0 for v in char.values())
        
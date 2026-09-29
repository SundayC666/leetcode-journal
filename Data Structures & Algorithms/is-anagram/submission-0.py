class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        l1 = []
        l2 = []
        for i in s:
            l1 += i
        
        for p in t:
            l2 += p

        if sorted(l1) == sorted(l2):
            return True
        else:
            return False
        
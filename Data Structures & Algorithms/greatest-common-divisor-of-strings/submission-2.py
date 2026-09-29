class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        s1 = len(str1)
        s2 = len(str2)
        
        def isDivisor(i):
            if s1 % i or s2 % i:
                return False
            f1, f2 = s1 // i, s2 // i
            return str1[:i] * f1 == str1 and str1[:i] * f2 == str2

        for i in range(min(s1,s2),0,-1):
            if isDivisor(i):
                return str1[:i]
        return ""

class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        len1 = len(word1)
        len2 = len(word2)
        len3 = []

        for i in range(max(len1, len2)):
            if len1 > i:
                len3.append(word1[i])
            if len2 > i:
                len3.append(word2[i])
            i += 1
        return "".join(len3)
            

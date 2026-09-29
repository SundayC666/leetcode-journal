class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        w1 = len(word1)
        w2 = len(word2)
        w3 = []
        for i in range(max(w1, w2)):
            if i < w1:
                w3.append(word1[i])
            if i < w2:
                w3.append(word2[i])
        return "".join(w3)
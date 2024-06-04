class Solution:
    def maxRepeating(self, sequence: str, word: str) -> int:
        quantidade = 0
        inicio = word
        while(word in sequence):
            quantidade += 1
            word = word + inicio
        return quantidade

print(Solution().maxRepeating("aaabaaaabaaabaaaabaaaabaaaabaaaaba", "aaaba"))


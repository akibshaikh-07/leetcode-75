# Problem: 1768. Merge Strings Alternately
# Link: https://leetcode.com/problems/merge-strings-alternately/
# Difficulty: Easy
# Topic: Array / String
# Approach: Used one index i that moves through both words. The loop runs while either word has characters left,
#           and appends the character from word1 and then from word2 if they exist. Joined the list at the end.
# Concept: Strings, two words, index loop, list + join

class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        result = []

        i = 0
        while i < len(word1) or i < len(word2):
            if i < len(word1):
                result.append(word1[i])

            if i < len(word2):
                result.append(word2[i])

            i += 1

        return "".join(result)

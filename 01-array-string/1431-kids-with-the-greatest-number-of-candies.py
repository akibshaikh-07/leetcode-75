# Problem: 1431. Kids With the Greatest Number of Candies
# Link: https://leetcode.com/problems/kids-with-the-greatest-number-of-candies/
# Difficulty: Easy
# Topic: Array
# Approach: First find the maximum number of candies among all kids.
#           Then check if each kid can reach or exceed the maximum after receiving extraCandies.
# Concept: Arrays, max(), comparison

class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        max_candies = max(candies)

        result = []

        for candy in candies:
            if candy + extraCandies >= max_candies:
                result.append(True)
            else:
                result.append(False)

        return result

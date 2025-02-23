from typing import List


class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        result = []
        def dfs(indices: List[int]):
            if len(indices) == len(nums):
                result.append(list(map(lambda i: nums[i], indices)))
            for i in range(len(nums)):
                if i not in indices:
                    dfs(indices + [i])
        dfs([])
        return list(map(list, set(map(tuple, result))))

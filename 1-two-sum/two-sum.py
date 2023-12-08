class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        from itertools import combinations

        for i,j in combinations(range(len(nums)), 2):
            if nums[i] + nums[j] == target:
                return [i,j]
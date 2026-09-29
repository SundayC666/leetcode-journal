class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}
        for i, val in enumerate(nums):
            n = target - val
            if n in seen:
                return [seen[n], i]
            seen[val] = i
        return []



        
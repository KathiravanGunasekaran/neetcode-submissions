class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        a = {}
        for i in range(len(nums)):
            needed = target - nums[i]
            if needed in a:
                return [a[needed], i]
            a[nums[i]] = i
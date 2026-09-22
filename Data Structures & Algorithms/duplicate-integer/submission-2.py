class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        set_a = set()
        for num in nums:
            if num in set_a:
                return True
            else:
                set_a.add(num)
        return False
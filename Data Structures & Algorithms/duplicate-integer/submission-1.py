class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        temp = {}
        is_duplicate_available = False
        for num in nums:
            if num not in temp:
                temp[num] = 1
            elif num in temp:
                temp[num] = temp[num] + 1
                is_duplicate_available = True
        return is_duplicate_available
        
        
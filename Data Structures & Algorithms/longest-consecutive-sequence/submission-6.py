class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums = set(nums)
        longest = 0
        if len(nums)==0:
            return 0
        if len(nums) ==1:
            return 1
        else:
            for num in nums:
                if num-1 not in nums:
                    current = num
                    length = 1

                    while current+1 in nums:
                        current = current+1
                        length = length+1
                    longest = max(longest, length)
        return longest

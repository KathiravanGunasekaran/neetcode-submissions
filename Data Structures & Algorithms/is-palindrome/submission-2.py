class Solution:
    def isPalindrome(self, s: str) -> bool:
        left = 0
        right = len(s) -1
        lowercase = s.lower()
        while left < right:
            while left < right and not lowercase[left].isalnum():
                left=left+1
            while right > left and not lowercase[right].isalnum():
                right=right-1


            if lowercase[left] != lowercase[right]:
                return False
            
            left = left+1
            right = right -1
        return True
            
        
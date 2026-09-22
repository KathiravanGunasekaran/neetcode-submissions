class Solution:
    def count_char(self, s):
        a = {}
        for c in s:
            if c in a:
                a[c] = a[c] +1
            else:
                a[c] = 1
        return a

    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        s_char_count = self.count_char(s)
        t_char_count = self.count_char(t)
        if t_char_count == s_char_count:
            return True
        else:
            return False
        

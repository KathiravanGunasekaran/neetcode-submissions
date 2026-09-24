class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        nums.sort()
        output=[]
        for i in range(len(nums)):
            if i>0 and nums[i-1] == nums[i]:
                continue
            l = i+1
            r = n-1
        
            while l<r:
                sum_s = nums[i]+nums[l]+nums[r]
                if(sum_s == 0):
                    output.append([nums[i],nums[l],nums[r]])
                    while l<r and nums[l] == nums[l+1]:
                        l=l+1
                    while l<r and nums[r] == nums[r-1]:
                        r=r-1
                    l=l+1
                    r=r-1
                elif(sum_s>0):
                    r= r-1
                else:
                    l=l+1
        return output


        



class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        frequency = {}
        ans=[]
        for num in nums:
            if num in frequency:
                frequency[num]= frequency[num] + 1
            else:
                frequency[num] = 1
        count_arr = []
        for num, count in frequency.items():
            count_arr.append([count, num])
        count_arr.sort()

        reversed_arr = count_arr[::-1]
        for i in range(k):
            ans.append(reversed_arr[i][1])
        return ans

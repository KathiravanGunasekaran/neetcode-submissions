class Solution:
    def maxArea(self, heights: List[int]) -> int:
        n = len(heights)
        l=0
        r = n-1
        m_area=0
        while l<r:
            width = r-l
            height = min(heights[r],heights[l])
            area = height*width

            if(m_area<area):
                m_area=area
            
            if(heights[r]<heights[l]):
                r=r-1
            else:
                l=l+1
        return m_area

class Solution:
    def maxArea(self, height: list[int]) -> int:
        best_area: int = 0
        left: int = 0
        right: int = len(height) - 1

        while left < right:
            area: int = min(height[left], height[right]) * (right - left)
            best_area = max(best_area, area)
            
            if height[left] < height[right]:
                left +=1
            else:
                right -= 1

        
        
        return best_area


# print(Solution().maxArea([1,8,6,2,5,4,8,3,7]))
# print(Solution().maxArea([1,1]))
# print(Solution().maxArea([1,2,4,3]))
# print(Solution().maxArea([1,3,2,5,25,24,5]))
print(Solution().maxArea([76,155,15,188,180,154,84,34,187,142,22,5,27,183,111,128,50,58,2,112,179,2,100,111,115,76,134,120,118,103,31,146,58,198,134,38,104,170,25,92,112,199,49,140,135,160,20,185,171,23,98,150,177,198,61,92,26,147,164,144,51,196,42,109,194,177,100,99,99,125,143,12,76,192,152,11,152,124,197,123,147,95,73,124,45,86,168,24,34,133,120,85,81,163,146,75,92,198,126,191]))
# ans = 18048



        # Get sorted highest values
        # Compare from highest to down inside original array
        # using two pointers make array of arrays sorted and containing index
        # and their value
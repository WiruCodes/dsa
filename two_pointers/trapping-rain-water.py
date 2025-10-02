class Solution:
    def trap(self, height: list[int]) -> int:
        left = 0
        right = len(height) - 1
        left_max = height[left]
        right_max = height[right]
        water = 0

        while left < right:
            if left_max < right_max:
                left += 1
                left_max = max(left_max, height[left])
                water += left_max - height[left]
            else:
                right -= 1
                right_max = max(right_max, height[right])
                water += right_max - height[right]

        return water


print(Solution().trap([0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]))
print(Solution().trap([4, 2, 0, 3, 2, 5]))


# * Slightly different solution by finding out limit by the min of
# * each side
# class Solution:
#     def trap(self, height: list[int]) -> int:
#         if len(height) == 1:
#             return 0

#         total: int = 0
#         collection_limit: int = 0
#         left: int = 0
#         right: int = len(height) - 1

#         while left < right:

#             collection_limit = max(collection_limit, min(height[left], height[right]))


#             if height[left] < height[right]:
#                 left += 1
#                 if collection_limit > 0 and height[left] < collection_limit:
#                     total += collection_limit - height[left]
#             else:
#                 right -= 1
#                 if collection_limit > 0 and height[right] < collection_limit:
#                     total += collection_limit - height[right]

#         return total


# class Solution:
#     def trap(self, height: list[int]) -> int:
#         total: int = 0
#         left: int = 0
#         right: int = len(height) - 1
#         left_max: int = 0
#         right_max: int = 0

#         while left < right:
#             if height[left] < height[right]:
#                 if height[left] >= left_max:
#                     left_max = height[left]
#                 else:
#                     total += left_max - height[left]
#                 left += 1
#             else:
#                 if height[right] >= right_max:
#                     right_max = height[right]
#                 else:
#                     total += right_max - height[right]
#                 right -= 1
#         return total

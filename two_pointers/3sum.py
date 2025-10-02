class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        nums.sort()
        if len(nums) == 0 or nums[0] > 0:
            return []

        ans_arr: list[list[int]] = []

        for idx in range(len(nums)):
            if nums[idx] > 0:
                break

            if idx > 0 and nums[idx] == nums[idx - 1]:
                continue

            left = idx + 1
            right = len(nums) - 1

            while left < right:
                total = nums[idx] + nums[left] + nums[right]

                if total == 0:
                    ans_arr.append([nums[idx], nums[left], nums[right]])

                    while left < right and nums[left] == nums[left + 1]:
                        left += 1
                    while left < right and nums[right] == nums[right - 1]:
                        right -= 1

                    left += 1
                    right -= 1

                elif left < right and total < 0:
                    left += 1
                else:
                    right -= 1

        return ans_arr


# print(Solution().threeSum([-1, 0, 1, 2, -1, -4]))
print(Solution().threeSum([2, -3, 0, -2, -5, -5, -4, 1, 2, -2, 2, 0, 2, -4, 5, 5, -10]))

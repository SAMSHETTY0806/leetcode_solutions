# class Solution:
#     def searchRange(self, nums: List[int], target: int) -> List[int]:
#         from bisect import bisect_left, bisect_right
# class Solution:
#     def searchRange(self, nums: List[int], target: int) -> List[int]:
#         if not nums:
#             return -1,-1
#         first = bisect_left(nums,target)

#         if first == len(nums) or nums[first] != target:
#             return -1,-1

#         last = bisect_right(nums,target) - 1

#         return first,last
class Solution:
    def searchRange(self, nums, target):
        def firstPos():
            left, right = 0, len(nums) - 1
            ans = -1

            while left <= right:
                mid = (left + right) // 2

                if nums[mid] == target:
                    ans = mid
                    right = mid - 1  # search left part
                elif nums[mid] < target:
                    left = mid + 1
                else:
                    right = mid - 1

            return ans

        def lastPos():
            left, right = 0, len(nums) - 1
            ans = -1

            while left <= right:
                mid = (left + right) // 2

                if nums[mid] == target:
                    ans = mid
                    left = mid + 1   # search right part
                elif nums[mid] < target:
                    left = mid + 1
                else:
                    right = mid - 1

            return ans

        return [firstPos(), lastPos()]

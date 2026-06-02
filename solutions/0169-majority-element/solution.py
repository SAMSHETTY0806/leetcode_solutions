# class Solution:
#     def majorityElement(self, nums):
#         count = 0
#         candidate = None

#         for num in nums:
#             if count == 0:
#                 candidate = num

#             if num == candidate:
#                 count += 1
#             else:
#                 count -= 1

#         return candidate
class Solution:
    def majorityElement(self, nums):
        freq = {}

        for num in nums:
            freq[num] = freq.get(num, 0) + 1

        for num in freq:
            if freq[num] > len(nums) // 2:
                return num

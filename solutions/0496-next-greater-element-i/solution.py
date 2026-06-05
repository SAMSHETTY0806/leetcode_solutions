class Solution:
    def nextGreaterElement(self, nums1, nums2):
        res = []
        for num in nums1:
            index = nums2.index(num)
            next_greater = -1
            for j in range(index + 1, len(nums2)):
                if nums2[j] > num:
                    next_greater = nums2[j]
                    break
            res.append(next_greater)
        return res

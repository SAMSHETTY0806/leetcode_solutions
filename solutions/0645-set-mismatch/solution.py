class Solution(object):
    def findErrorNums(self, nums):
        duplicate = -1
        n = len(nums)

        s = set()

        for num in nums:
            if num in s:
                duplicate = num
            s.add(num)

        for i in range(1, n + 1):
            if i not in s:
                missing = i
                break

        return [duplicate, missing]

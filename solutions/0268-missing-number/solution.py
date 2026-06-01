class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n=len(nums)
        sums=n*(n+1)//2
        mis=sums-(sum(nums))
        return mis

        

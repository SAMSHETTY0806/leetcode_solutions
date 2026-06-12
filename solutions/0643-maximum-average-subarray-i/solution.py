class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:

        s = sum(nums[:k])   
        c = s               

        for i in range(k, len(nums)):
            c += nums[i] - nums[i - k]   
            if c > s:
                s = c                    

        return s / k                     # Divide once at the end

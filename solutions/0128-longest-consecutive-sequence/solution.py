class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        s = set(nums)
        count = 0           
        for i in s:             
            if i - 1 not in s:  
                j = i
                while j in s:
                    j += 1
                count = max(count, j - i)
        return count

        

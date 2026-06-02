class Solution:
    def findPairs(self, nums: List[int], k: int) -> int:
        if k < 0:
            return 0
        
        d = {}
        for i in nums:
            d[i] = d.get(i, 0) + 1
        
        count = 0
        
        for key in d:
            if k == 0:
                if d[key] >= 2:
                    count += 1
            else:
                if key + k in d:
                    count += 1
        
        return count

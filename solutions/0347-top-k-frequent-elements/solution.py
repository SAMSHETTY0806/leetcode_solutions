from collections import Counter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count=Counter(nums)
        s=sorted(count.items(),key=lambda x:x[1],reverse=True)
        res=[]
        for num,freq in s:
            res.append(num)
            if len(res)==k:
                return res
        

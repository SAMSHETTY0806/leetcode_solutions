class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        min=prices[0]
        max=0

        for p in prices:
            if p<min:
                min=p
            p=p-min
            if p>max:
                max=p
        return max

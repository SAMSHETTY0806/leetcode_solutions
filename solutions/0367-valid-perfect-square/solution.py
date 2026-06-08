class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        sqr=0
        while sqr*sqr <= num:
            if sqr*sqr == num:
                return True 
            sqr+=1
        return False
        

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        left=0
        right=len(matrix)-1
        while left<=right:
            mid=(left+right)//2
            f=matrix[mid]
            l=0
            r=len(f)-1
            while l<=r:
                m=(l+r)//2
                if f[m]==target:
                    return True
                elif f[m]>target:
                    r=m-1
                else:
                    l=m+1
            if f[-1]>target:
                right=mid-1
            elif f[-1]<target:
                left=mid+1
        return False
        

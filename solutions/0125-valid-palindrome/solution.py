class Solution:
    def isPalindrome(self, s: str) -> bool:
        s=s.lower()
        res=""
        for char in s:
            if char.isalnum():
                res +=char
        if res==res[::-1]:
            return True
        else:
            return False
        
        

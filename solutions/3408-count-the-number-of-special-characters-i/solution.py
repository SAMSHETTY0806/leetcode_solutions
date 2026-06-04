class Solution:
    def numberOfSpecialChars(self, word: str) -> int:
        char=set(word)
        count=0
        for i in char:
            if i.islower() and i.upper() in char :
                count+=1
        return count
        

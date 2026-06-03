class Solution:
    def reverseVowels(self, s: str) -> str:
        vow="aeiouAEIOU"
        i=0
        j=len(s)-1
        l=list(s)
        while i<j:
            if l[i] not in vow:
                i+=1
            elif l[j] not in vow:
                j-=1
            else:
                l[i],l[j]=l[j],l[i]
                i+=1
                j-=1
        return "".join(l)

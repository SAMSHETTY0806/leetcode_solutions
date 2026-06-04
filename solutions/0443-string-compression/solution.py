class Solution:
    def compress(self, chars: List[str]) -> int:
        a=0
        i=0
        while(i<len(chars)):
            res=chars[i]
            count=0
            while (i<len(chars))and chars[i]==res:
                count+=1
                i+=1
            chars[a]=res
            a+=1
            if count>1:
                for c in str(count):
                    chars[a]=c
                    a+=1
        return a

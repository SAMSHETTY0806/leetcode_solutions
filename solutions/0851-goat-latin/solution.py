class Solution:
    def toGoatLatin(self, sentence: str) -> str:
        s=[]
        v=set("aeiouAEIOU")
        for i , word in enumerate(sentence.split(),1):
            if word[0] in v:
                goat=word+"ma"
            else:
                goat=word[1:]+word[0]+"ma"
            s.append(goat+"a"*i)
        return " ".join(s)
                

        

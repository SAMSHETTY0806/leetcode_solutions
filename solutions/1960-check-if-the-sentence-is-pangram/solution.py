class Solution:
    def checkIfPangram(self, sentence: str) -> bool:

        r=set(sentence)
        if len(r)==26:
            return True
        else:
            return False

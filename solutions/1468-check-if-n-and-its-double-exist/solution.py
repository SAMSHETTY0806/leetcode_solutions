class Solution:
    def checkIfExist(self, arr):
        a = set()

        for num in arr:
            if num * 2 in a or (num % 2 == 0 and num // 2 in a):
                return True
            a.add(num)

        return False

class Solution:
    def isHappy(self, n: int) -> bool:
        a= set()

        while n != 1:
            if n in a:
                return False
            a.add(n)

            n = sum(int(d) ** 2 for d in str(n))

        return True

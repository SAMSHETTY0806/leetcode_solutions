class Solution:
    def countStudents(self, students, sandwiches):
        count0 = students.count(0)
        count1 = students.count(1)

        for i, s in enumerate(sandwiches):
            if s == 0:
                if count0 == 0:
                    return len(sandwiches) - i
                count0 -= 1
            else:
                if count1 == 0:
                    return len(sandwiches) - i
                count1 -= 1

        return 0

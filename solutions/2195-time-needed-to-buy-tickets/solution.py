from collections import deque

class Solution:
    def timeRequiredToBuy(self, tickets, k):
        q = deque(range(len(tickets)))
        time = 0

        while q:
            i = q.popleft()
            tickets[i] -= 1
            time += 1

            if tickets[i] == 0:
                if i == k:
                    return time
            else:
                q.append(i)

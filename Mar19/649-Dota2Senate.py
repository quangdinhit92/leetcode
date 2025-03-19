class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        n = len(senate)
        radian = deque()
        dire = deque()

        for i, s in enumerate(senate):
            if "D" == s:
                dire.append(i)
            else:
                radian.append(i)

        while dire and radian:
            d = dire.popleft()
            r = radian.popleft()
            if r < d:
                # radian win add radian to end of queue
                radian.append(r + n)
            else:
                dire.append(d + n)

        if len(dire) == 0:
            return "Radiant"
        if len(radian) == 0:
            return "Dire"

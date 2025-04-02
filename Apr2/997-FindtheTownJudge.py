class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:

        whoTrust = [0] * n
        whoTrusted = [0] * n
        for i in range(len(trust)):
            action = trust[i]
            toTrust = action[0] - 1
            toBeTrusted = action[1] - 1
            whoTrust[toTrust] += 1
            whoTrusted[toBeTrusted] += 1

        for i in range(n):
            if 0 == whoTrust[i] and whoTrusted[i] >= n - 1:
                return i + 1
        return -1

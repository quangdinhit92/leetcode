class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        n = len(candidates)
        solutions = []
        ans = []

        def makeCombinenation(idx, total):

            if total == 0:
                solutions.append(ans.copy())
                return

            if idx >= n or total < 0:
                return

            chose = candidates[idx]
            ans.append(chose)
            makeCombinenation(idx, total - chose)
            ans.pop()
            makeCombinenation(idx + 1, total)

        makeCombinenation(0, target)
        return solutions

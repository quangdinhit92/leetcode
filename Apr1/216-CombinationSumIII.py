class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:

        ret = []

        def combine(curIndex, combinations):
            if curIndex >= k:
                if sum(combinations) == n:
                    if combinations not in ret:
                        ret.append(combinations.copy())
                return
            for i in range(1, 10):
                if i not in combinations:
                    combinations.add(i)
                    combine(curIndex + 1, combinations)
                    combinations.remove(i)

        combine(0, set())
        return [list(item) for item in ret]

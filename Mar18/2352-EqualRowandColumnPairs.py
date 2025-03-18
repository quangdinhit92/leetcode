class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        count = 0
        dictColumn = dict()

        for i in range(len(grid[0])):
            col = []
            for j in range(len(grid)):
                col.append(grid[j][i])
            dictColumn[str(col)] = dictColumn.get(str(col), 0) + 1

        for row in grid:
            count += dictColumn.get(str(row), 0)

        return count

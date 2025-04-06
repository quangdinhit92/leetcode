class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        # directs=[[-1,0],[0,-1],[+1,0],[0,+1]]
        directions = {"top": [-1, 0], "left": [0, -1], "bot": [+1, 0], "right": [0, +1]}

        q = deque()
        unrotted = 0
        minutes = 0
        for r in range(m):
            for c in range(n):
                if 2 == grid[r][c]:
                    q.append((r, c, 0))
                elif 1 == grid[r][c]:
                    unrotted += 1

        while q:
            for _ in range(len(q)):
                r, c, t = q.popleft()
                minutes = max(minutes, t)
                for d in directions.keys():
                    dct = directions[d]

                    nr, nc = r + dct[0], c + dct[1]
                    if 0 <= nr < m and 0 <= nc < n and 1 == grid[nr][nc]:
                        q.append((nr, nc, t + 1))
                        grid[nr][nc] = 2
                        unrotted -= 1

        if 0 == unrotted:
            return minutes
        return -1

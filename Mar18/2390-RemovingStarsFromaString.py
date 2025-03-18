class Solution:
    def removeStars(self, s: str) -> str:
        queue = deque()
        for ch in s:
            if ch != "*":
                queue.append(ch)
            else:
                queue.pop()
        return "".join(list(queue))

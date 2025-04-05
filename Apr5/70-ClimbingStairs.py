class Solution:
    solutions = 0

    def climbStairs(self, n: int) -> int:
        dp = [0] * (n + 1)

        def jump(step):

            if 0 == step:
                return 1
            if step < 0:
                return 0
            r0 = 0
            r1 = 0
            if step - 1 >= 0:
                if 0 == dp[step - 1]:
                    r0 = jump(step - 1)
                else:
                    r0 = dp[step - 1]
            if step - 2 >= 0:
                if 0 == dp[step - 2]:
                    r1 = jump(step - 2)
                else:
                    r1 = dp[step - 2]

            dp[step] = r0 + r1

            return r1 + r0

        tmp = jump(n)
        return tmp
